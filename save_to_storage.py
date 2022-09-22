from google.cloud import storage

from config import BUCKET_NAME, BUCKET_FILE_NAME, FILENAME


def save_file():
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(BUCKET_FILE_NAME)
    blob.upload_from_filename(FILENAME)
