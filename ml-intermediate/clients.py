from ploomber.clients import S3Client, GCloudStorageClient


def get_s3():
    return S3Client(bucket_name='bucket-name',
                    parent='ml-intermediate',
                    json_credentials_path='credentials.json')


def get_gcloud():
    return GCloudStorageClient(bucket_name='bucket-name',
                               parent='ml-intermediate',
                               json_credentials_path='credentials.json')
