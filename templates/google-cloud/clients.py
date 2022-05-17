from google.cloud.bigquery.dbapi import connect
from ploomber.clients import DBAPIClient, GCloudStorageClient


def db():
    return DBAPIClient(connect, dict())


def storage():
    return GCloudStorageClient(bucket_name='my-ploomber-bucket',
                               parent='my-pipeline')
