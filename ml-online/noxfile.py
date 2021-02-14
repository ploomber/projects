"""
nox configuration file.
docs: https://nox.thea.codes/en/stable/index.html
"""
import nox


@nox.session(venv_backend='conda', python='3.8')
def tests(session):
    session._run('conda', 'env', 'update', '--prefix',
                 session.virtualenv.location, '--file', 'environment.yml')

    session.install('--editable', '.[dev]')

    session.run('ploomber', 'build')

    session.run('cp', 'products/model.pickle', 'src/ml-online/model.pickle')

    session.run('pytest', 'tests/')

    print('Generatnig environment.lock.yml...')
    session.run('conda', 'env', 'export', '--prefix',
                session.virtualenv.location, '--file', 'environment.lock.yml')
