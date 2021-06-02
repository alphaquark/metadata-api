import os
import logging
import uuid

from flask import Flask,jsonify,request,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename
from boto3.s3.transfer import TransferConfig

from s3client import s3connection

MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")

LOCAL_UPLOAD_PATH = os.environ.get("LOCAL_UPLOAD_PATH")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
BUCKET_PATH = os.environ.get("BUCKET_PATH")
S3_PATH_PREFIX = os.environ.get("S3_PATH_PREFIX")

MB = 1024**2

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

app = Flask("__name__")
CORS(app, resources={r'*': {'origins': '*'}})
#CORS(app, resources={r'*': {'origins': 'https://nft.alphaquark.io', 'https://nft.alphaquark.io'}})

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@db:3306/{MYSQL_DATABASE}"
db = SQLAlchemy(app)

def _add_attribute(existing, attribute_name, options):
    trait = {
        'trait_type': attribute_name,
        'value': options
    }
    existing.append(trait)

@app.route('/contract/info')
def contractInfo():
    return json_response({
        'name': 'AlphaQuark NFT',
        'description': 'Intellectual property backed NFT items powered by Alpha Quark',
        'image' : 'https://ipfs.io/ipfs/QmVUhm56KnARNsuqf2rewR1yAeZEaUuFUaN4h5Ek8xQzAP',
        'external_url' : 'https://nft.alphaquark.io',
        #'seller_fee_basis_points': 500, # Indicates a 5% seller fee.
        #'fee_recipient': '0xA0346C590Dd9baE8F74E1A8b332ff5184c784A57' # Where seller fees will be paid to.
    },200)

@app.route('/api/<token_id>',methods=['GET'])
def get_by_id(token_id):
    from models import Metadata,MetadataSchema

    #현재 row 갯수 확인하면서 db 오류 체크
    try:
        current_row_length = len(Metadata.query.all())
    except Exception as ex:
        logging.error(f"{ex}")
        return json_response(f"{{'error': {ex}}}",500)

    #request parameter 정수 체크
    try:
        token_id = int(token_id)
    except:
        return json_response({'error' : 'token_id is not integer'},500)

    #request parameter 유효 범위 체크
    if token_id > current_row_length or token_id < 1:
        return json_response({'error' : 'out of token_id range'},500)
    
    try:
        get_metadata = Metadata.query.get(token_id)
        metadata_schema = MetadataSchema()
        
        metadata = metadata_schema.dump(get_metadata)   

        attributes = []
        _add_attribute(attributes, 'cover-image', metadata["cover_image"])
        _add_attribute(attributes, 'video-uri', metadata["video_uri"])
        _add_attribute(attributes, 'preview-uri', metadata["preview_uri"])
        _add_attribute(attributes, 'source-uri', metadata["source_uri"])
        _add_attribute(attributes, 'song-name', metadata["song_name"])
        _add_attribute(attributes, 'singer', metadata["singer"])
        _add_attribute(attributes, 'song-by', metadata["song_by"])
        _add_attribute(attributes, 'lyrics-by', metadata["lyrics_by"])
        _add_attribute(attributes, 'arrangement', metadata["arrangement"])
        _add_attribute(attributes, 'publish-date', metadata["publish_date"])
        _add_attribute(attributes, 'serial-number', metadata["serial_number"])
        _add_attribute(attributes, 'introduction', metadata["introduction"])

        return json_response({
            'name': metadata["name"],
            'description': metadata["description"],
            'image':  metadata["image"],
            'external_url': metadata["external_url"],
            'attributes': attributes
        },200)

    except Exception as ex:
        print(f"error: {ex}")
        return json_response(f"{{'error': {ex}}}",500)

@app.route('/api', methods=['GET','POST'])
def create_metadata():
    try:
        from models import MetadataSchema

        data = request.get_json()
        metadata_schema = MetadataSchema()
        metadata = metadata_schema.load(data,session=db.session)
        result = metadata_schema.dump(metadata.create())
        return json_response({'metadata': result},200)
    
    except Exception as ex:
        logging.error(f'{ex}')
        return json_response(f"{{'error': {ex}}}",500)

@app.route('/api/upload', methods=['GET','POST'])
def upload_file():    
    if request.method == 'POST':
        try:
            upload_file = request.files['file']
            if upload_file:
                secure_file_name = secure_filename(upload_file.filename)
                content_type = secure_file_name.rpartition('.')[-1]
                temp_file_name=f"{uuid.uuid4().hex}.{content_type}"

                #local upload
                target=os.path.join(LOCAL_UPLOAD_PATH,'temp')
                if not os.path.isdir(target):
                    os.mkdir(target)
                temp_upload_path = "/".join([target, temp_file_name])
                upload_file.save(temp_upload_path)
                logging.info(f"local file upload completed : {temp_file_name}")

                #s3 upload                
                s3_path = f"{BUCKET_PATH}{temp_file_name}"
                s3 = s3connection()

                config = TransferConfig(multipart_threshold=10*MB)
                s3.upload_file(temp_upload_path,BUCKET_NAME,s3_path,Config=config)

                s3_path = f"{S3_PATH_PREFIX}/{s3_path}"
                logging.info(f"s3 file upload completed : {s3_path}")
                # remove temp
                os.remove(temp_upload_path)
                logging.info(f"local file remove completed : {temp_upload_path}")

                return json_response({'s3_path': s3_path},200)

        except Exception as ex:
            logging.error(f'{ex}')
            return json_response(f"{{'error': {ex}}}",500)

def json_response(jsondata,http_status_code):
    return make_response(jsonify(jsondata),http_status_code)

if __name__=='__main__':
    app.run(host='0.0.0.0')