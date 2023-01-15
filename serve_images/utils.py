import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config
import os


def fetch_s3_images():
    images_urls = []
    os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"
    # s3://oguploadmaster/portalUploads/ahm2021/aainphotos/
    s3 = boto3.resource('s3',config=Config(signature_version=UNSIGNED))
    s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    my_bucket = s3.Bucket('testbucketfp')
    for my_bucket_object in my_bucket.objects.all():
        # print(my_bucket_object.key)
        response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': 'testbucketfp',
                                                                'Key': my_bucket_object.key},
                                                        ExpiresIn=3600)
        images_urls.append(response)
    return images_urls


# Completing in a while  


# from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def fetch_google_images():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'serve_images\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        folder_id = '1_qOJ0z3kI_e2IJq4X6HqF0T1ROBESygS' # Same folder ID as above
        query = "'%s' in parents" % folder_id
        results = service.files().list(q=query, pageSize=1000, 
                                        includeItemsFromAllDrives=True, 
                                        supportsAllDrives=True, 
                                        corpora="allDrives", 
                                        fields='files(webViewLink)').execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        response = []
        for item in items:
            response.append(item['webViewLink'])
        return response
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
