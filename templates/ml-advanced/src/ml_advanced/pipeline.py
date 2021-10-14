"""
Pipeline declaration using ploomber:

https://github.com/ploomber/ploomber
"""
from ploomber import with_env, DAGConfigurator, SourceLoader
from ploomber.tasks import PythonCallable, NotebookRunner
from ploomber.products import File
from ploomber.executors import Parallel

from ml_advanced import tasks


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

    # run this in parallel
    dag.executor = Parallel(processes=3)

    loader = SourceLoader(module='ml_advanced.templates')

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

    get >> fts

    (get + fts) >> join

    model_classes = [
        'sklearn.ensemble.RandomForestClassifier',
        # these come from our package, they return a sklearn Pipeline object
        'ml_advanced.models.logistic_reg',
        'ml_advanced.models.svc',
    ]

    model_param_grids = [
        dict(n_estimators=[5, 10, 50, 100], min_samples_leaf=[2, 4, 8]),
        dict(clf__penalty=['l1', 'l2'], clf__C=[0.5, 1.0]),
        dict(clf__kernel=['linear', 'poly', 'rbf'], clf__C=[0.5, 1.0]),
    ]

    for model_class, model_params in zip(model_classes, model_param_grids):
        fit = NotebookRunner(
            loader['fit.py'],
            product={
                'nb': File(env.path.data / f'fit-{model_class}.ipynb'),
                'model': File(env.path.data / f'model-{model_class}.joblib')
            },
            dag=dag,
            params={
                'model_class': model_class,
                'model_params': model_params
            },
            # NOTE: Argo does not support "." nor  "_" in task names. Not
            # needed if only running locally
            name='fit-' + model_class.replace('.', '--').replace('_', '-'))

        join >> fit

    return dag
