"""
Module to create connections to the database
"""
from ploomber.clients import SQLAlchemyClient


def get_client():
    return SQLAlchemyClient('sqlite:///data.db')
