"""
Pipeline declaration using ploomber:

https://github.com/ploomber/ploomber
"""
from ploomber import with_env, DAGConfigurator
from ploomber.tasks import PythonCallable
from ploomber.products import File

from basic_ml import tasks


@with_env
def make(env):
    """
    Make pipeline

    Returns
    -------
    ploomber.DAG
        A pipeline object

    Notes
    -----
    This is a numpy docstring, which is the standard format in the Python data
    ecosystem: https://numpydoc.readthedocs.io/en/latest/format.html
    """
    # this function is used by the entry points to automatically initialize
    # the env in env.yaml
    return _make(env)


def _make(env):
    # this is the private function we use to pass the testing environment
    cfg = DAGConfigurator(env.dag_config)
    dag = cfg.create(name='ml-pipeline')

    get = PythonCallable(tasks.get,
                         File(env.path.data / 'data.parquet'),
                         dag,
                         name='get',
                         params={'sample_frac': env.sample_frac})

    fts = PythonCallable(tasks.features,
                         File(env.path.data / 'features.parquet'),
                         dag,
                         name='features')
    join = PythonCallable(tasks.join,
                          File(env.path.data / 'join.parquet'),
                          dag,
                          name='join')

    fit = PythonCallable(tasks.fit, {'report':
                                     File(env.path.data / 'report.txt'),
                                     'model':
                                     File(env.path.data / 'model.joblib')},
                         dag,
                         name='fit')

    get >> fts

    (get + fts) >> join

    join >> fit

    return dag
