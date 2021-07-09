from ploomber.clients import SQLAlchemyClient


def get():
    return SQLAlchemyClient('sqlite:///my.db')