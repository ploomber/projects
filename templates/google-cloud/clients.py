from google.cloud.bigquery.dbapi import connect
from ploomber.clients import DBAPIClient


def get():
    return DBAPIClient(connect, dict())
