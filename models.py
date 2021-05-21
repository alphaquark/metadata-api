from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from datetime import datetime
from app import db

class Metadata(db.Model):
    __tablename__ = "metadata"   

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)    
    cover_image = db.Column(db.String(1000))
    video_uri = db.Column(db.String(1000))
    preview_uri = db.Column(db.String(1000))
    source_uri = db.Column(db.String(1000))
    song_name = db.Column(db.String(1000))
    singer = db.Column(db.String(1000))
    song_by = db.Column(db.String(1000))
    lyrics_by = db.Column(db.String(1000))
    arrangement = db.Column(db.String(1000))
    publish_date = db.Column(db.DateTime)
    serial_number = db.Column(db.String(1000))
    introduction = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    external_url = db.Column(db.String(1000))
    image = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime)
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __init__(   self,
                    cover_image,
                    video_uri,
                    preview_uri,
                    source_uri,
                    song_name,
                    singer,
                    song_by,
                    lyrics_by,
                    arrangement,
                    publish_date,
                    serial_number,
                    introduction,
                    description,
                    external_url,
                    image,
                    name,
                    ):
        self.cover_image = cover_image
        self.video_uri = video_uri
        self.preview_uri = preview_uri
        self.source_uri = source_uri
        self.song_name = song_name
        self.singer = singer
        self.song_by = song_by
        self.lyrics_by = lyrics_by
        self.arrangement = arrangement
        self.publish_date = publish_date
        self.serial_number = serial_number
        self.introduction = introduction
        self.description = description
        self.external_url = external_url
        self.image = image
        self.name = name
        self.created_at = datetime.now()

    def __repr__(self):
        return f"{self.id}"

class MetadataSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = Metadata
    id = fields.Number(dump_only=True)
    cover_image = fields.String(Required=False)
    video_uri = fields.String(Required=False)
    preview_uri = fields.String(Required=False)
    source_uri = fields.String(Required=False)
    song_name = fields.String(Required=False)
    singer = fields.String(Required=False)
    song_by = fields.String(Required=False)
    lyrics_by = fields.String(Required=False)
    arrangement = fields.String(Required=False)
    publish_date = fields.DateTime(Required=False,format='%Y-%m-%d')
    serial_number = fields.String(Required=False)
    introduction = fields.String(Required=False)
    description = fields.String(Required=False)
    external_url = fields.String(Required=False)
    image = fields.String(Required=False)
    name = fields.String(Required=False)
    created_at = fields.DateTime(Required=False)