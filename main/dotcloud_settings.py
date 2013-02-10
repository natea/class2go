import json

# For using S3 Storage, specify these with real settings
with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

try:
    AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'appsembler-class2go'
    AWS_SECURE_STORAGE_BUCKET_NAME = 'appsembler-secure-class2go' # Optional. If not defined here, it will be composed from the AWS_STORAGE_BUCKET_NAME in settings.py
except:
    AWS_ACCESS_KEY_ID = 'AAAAAAAAAAAAAAAAAAAA'
    AWS_SECRET_ACCESS_KEY = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    AWS_STORAGE_BUCKET_NAME = 'dev-c2g'
    AWS_SECURE_STORAGE_BUCKET_NAME = 'dev-secure-c2g' # Optional. If not defined here, it will be composed from the AWS_STORAGE_BUCKET_NAME in settings.py