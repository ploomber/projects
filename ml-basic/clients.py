from ploomber.clients import GCloudStorageClient


def get_storage_client():
    """Example client to upload artifacts to google cloud storage
    """
    return GCloudStorageClient(bucket_name='ploomber-test-bucket',
                               parent='ml-basic')
