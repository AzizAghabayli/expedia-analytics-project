import os
import glob
from kaggle.api.kaggle_api_extended import KaggleApi
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv
load_dotenv('./data.env')

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
project_id = os.getenv('GCP_PROJECT_ID')
bucket_name = os.getenv('GCS_BUCKET_NAME')
dataset_name = os.getenv('DATASET_NAME')

def download_dataset_from_kaggle(dataset_name, destination_directory):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset_name, path=destination_directory, unzip=True)
    print("Files downloaded and extracted successfully")

def upload_files_to_gcs(bucket_name, source_directory):
    files = glob.glob(os.path.join(source_directory, '*.csv'))
    for file_path in files:
        destination_blob_name = os.path.basename(file_path)
        upload_blob(bucket_name, file_path, destination_blob_name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        print(f"Failed to upload {source_file_name}: {e}")

if __name__ == "__main__":
    credentials = service_account.Credentials.from_service_account_file(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    storage_client = storage.Client(credentials=credentials, project=os.getenv('GCP_PROJECT_ID'))

    download_dataset_from_kaggle(os.getenv('DATASET_NAME'), "./raw")
    upload_files_to_gcs(os.getenv('GCS_BUCKET_NAME'), './raw')