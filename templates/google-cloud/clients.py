# %%
import sqlite3

# %%
from google.cloud.bigquery.dbapi import connect
from ploomber.clients import (DBAPIClient, GCloudStorageClient,
                              SQLAlchemyClient)

# %% [markdown]
# NOTE: you may use db or db_sqlalchemy. Both work the same


# %%
def db():
    """Client to send queries to BigQuery
    """
    return DBAPIClient(connect, dict())


# %%
def db_sqlalchemy():
    """Client to send queries to BigQuery (uses SQLAlchemy as backend)
    """
    # you may pass bigquery://{project-name} to use a specific project,
    # otherwise thiw will use the default one
    return SQLAlchemyClient('bigquery://')


# %%
def storage():
    """Client to upload files to Google Cloud Storage
    """
    # ensure your bucket_name matches
    return GCloudStorageClient(bucket_name='ploomber-bucket',
                               parent='my-pipeline')


# %%
def metadata():
    """
    (Optional) client to store SQL tasks metadata to enable incremental builds
    """
    return DBAPIClient(sqlite3.connect, dict(database='products/metadata.db'))
