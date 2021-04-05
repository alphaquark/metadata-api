'''

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 995075410133.dkr.ecr.ap-northeast-2.amazonaws.com

api
docker tag aqt-metadata_api:latest 995075410133.dkr.ecr.ap-northeast-2.amazonaws.com/aqt/metadata-api:0.1
docker push 995075410133.dkr.ecr.ap-northeast-2.amazonaws.com/aqt/metadata-api:0.1

nginx
docker tag aqt-metadata_nginx:latest 995075410133.dkr.ecr.ap-northeast-2.amazonaws.com/aqt/metadata-nginx:0.1
docker push 995075410133.dkr.ecr.ap-northeast-2.amazonaws.com/aqt/metadata-nginx:0.1
'''