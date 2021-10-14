from ploomber import with_env
from ploomber.clients import SQLAlchemyClient

@with_env
def get_client(env):
    path = env.path.products_root / 'data.db'

    # create parent folders if they don't exist, otherwise sqlalchemy fails
    if not path.parent.exists():
        path.parent.mkdir(exist_ok=True, parents=True)

    return SQLAlchemyClient(f'sqlite:///{path}')
