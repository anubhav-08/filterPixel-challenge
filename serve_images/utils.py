import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config
import os
from Google import Create_Service


def fetch_s3_images():
    images_urls = []
    os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"
    # s3://oguploadmaster/portalUploads/ahm2021/aainphotos/
    s3 = boto3.resource('s3',config=Config(signature_version=UNSIGNED))
    s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    my_bucket = s3.Bucket('testbucketfp')
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
        response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': 'testbucketfp',
                                                                'Key': my_bucket_object.key},
                                                        ExpiresIn=3600)
        images_urls.append(response)
    return images_urls



def fetch_google_images():

    CLIENT_SECRET_FILE = 'client-secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Update Sharing Setting
    file_id = '<file id>'

    request_body = {
        'role': 'reader',
        'type': 'anyone'
    }

    response_permission = service.permissions().create(
        fileId=file_id,
        body=request_body
    ).execute()

    print(response_permission)
    
    # Print Sharing URL
    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink'
    ).execute()

    print(response_share_link)

    # Remove Sharing Permission
    service.permissions().delete(
        fileId=file_id,
        permissionId='anyoneWithLink'
    ).execute()

