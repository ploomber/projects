import sqlite3

from google.cloud.bigquery.dbapi import connect
from ploomber.clients import (DBAPIClient, GCloudStorageClient,
                              SQLAlchemyClient)


def db():
    """Client to send queries to BigQuery
    """
    return DBAPIClient(connect, dict())


def db_sqlalchemy():
    """Client to send queries to BigQuery (uses SQLAlchemy as backend)
    """
    return SQLAlchemyClient('bigquery://')


def storage():
    """Client to upload files to Google Cloud Storage
    """
    return GCloudStorageClient(bucket_name='my-ploomber-bucket',
                               parent='my-pipeline')


def metadata():
    """
    (Optional) client to store SQL tasks metadata to enable incremental builds
    """
    return DBAPIClient(sqlite3.connect, dict(database='products/metadata.db'))