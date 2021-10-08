"""
Factories
=========

Non-trivial pipelines span multiple files to improve code organization and readability. To avoid global mutable state, the recommended approach is to create funcions that return task instances (task factories) that then will be called by a DAG factory to instantiate a DAG. A second advantage of using factories is that we can parametrize them to re-use the same task (or pipeline) factory multiple times.

This example shows how to build two pipelines that share the same code, and are customized by passing a different set of parameters. We'll be using the iris dataset, the first pipeline will analyze setosa observations and the second one virginica.
"""
import atexit
import shutil
from pathlib import Path
import tempfile

import pandas as pd
from sklearn import datasets

from ploomber import DAG, with_env, load_env
from ploomber.clients import SQLAlchemyClient
from ploomber.tasks import SQLUpload, SQLScript, PythonCallable, NotebookRunner
from ploomber.products import SQLiteRelation, File
from ploomber.executors import Serial


@atexit.register
def clean():
    """Helper function to ensure products/ is deleted when the Python interpreter shuts down
    """
    if Path('products').exists():
        shutil.rmtree('products')


def _dump(product, kind):
    """Dump data into a local file

    Parameters
    ----------
    kind
        Which data subset to use
    """
    d = datasets.load_iris()

    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']
    df['target'] = (df.target.replace(
        {i: name
         for i, name in enumerate(d.target_names)}))
    df = df[df['target'] == kind]

    df.to_parquet(str(product))


@load_env
def make_task_dump(env, dag, kind):
    """Returns a task instance using the _dump function

    Parameters
    ----------
    kind
        Sub-directory to store the output
    """
    return PythonCallable(_dump,
                          product=File(env.path / kind / 'raw.parquet'),
                          dag=dag,
                          name='raw',
                          params=dict(kind=kind))


@load_env
def make_task_upload(env, dag, kind):
    """Uploads the data to a SQLite database

    Parameters
    ----------
    kind
        Table name suffix
    """
    return SQLUpload('{{upstream["raw"]}}',
                     product=SQLiteRelation((None, f'raw_{kind}', 'table')),
                     dag=dag,
                     name='upload',
                     to_sql_kwargs={'if_exists': 'replace'})


@load_env
def make_task_clean(env, dag, kind):
    """Clean data

    Parameters
    ----------
    kind
        Table name suffix
    """
    sql = """
    CREATE TABLE {{product}} AS
    SELECT * FROM {{upstream['upload']}}
    """
    return SQLScript(sql,
                     product=SQLiteRelation((None, f'clean_{kind}', 'table')),
                     dag=dag,
                     name='clean')


@load_env
def make_task_report(env, dag, kind):
    report = """
from sqlalchemy import create_engine
import seaborn as sns
import pandas as pd
from IPython.display import Markdown

# + tags=['parameters']
db_uri = None
upstream = None
product = None
kind = None

# +
Markdown(f'# {kind}')

# +
engine = create_engine(db_uri)
query = 'SELECT * FROM {}'.format(upstream["clean"])
df = pd.read_sql(query, engine)
engine.dispose()

# ## sepal length 

# +
sns.distplot(df['sepal length (cm)'])
"""
    return NotebookRunner(report,
                          File(env.path / f'report-{kind}.html'),
                          dag,
                          ext_in='py',
                          name='report',
                          params={
                              'db_uri': env.db_uri,
                              'kind': kind
                          })


###############################################################################
# This introduces a subtle but important distinction between Env and Task.params,
# Env is a read-only object for storing configuration parameters
# (such as db URIs) where as Task.params are intended to customize a DAG
# behavior, for example, if you want to generate two reports for 2018 and 2019
# data, you can call the a DAG factory twice (both DAGs with the same Env)
# but one dag with the 2018 parameter and another one with the 2019 parameter


@with_env({
    'path': 'products',
    'db_uri': 'sqlite:///' + str(Path('products', 'my.db')),
})
def make_dag(env, kind):
    Path(env.path).mkdir(exist_ok=True, parents=True)

    dag = DAG(executor=Serial(build_in_subprocess=False))

    client = SQLAlchemyClient(env.db_uri)
    dag.clients[SQLUpload] = client
    dag.clients[SQLiteRelation] = client
    dag.clients[SQLScript] = client

    dump = make_task_dump(dag, kind)
    upload = make_task_upload(dag, kind)
    clean = make_task_clean(dag, kind)
    report = make_task_report(dag, kind)

    dump >> upload >> clean >> report

    return dag


###############################################################################
# Now multiple dag objects can be created easily. Note that although DAGs
# (and their tasks) are different objects, they still read from the same Env.

dags = {kind: make_dag(kind) for kind in ('setosa', 'virginica')}

###############################################################################
# Pipeline (setosa) status
# ------------------------

dags['setosa'].status()

###############################################################################
# Pipeline (virginica) status
# ------------------------

dags['virginica'].status()

###############################################################################
# Pipeline plots
# --------------

dags['setosa'].plot()

dags['virginica'].plot()

###############################################################################
# Pipelines build
# --------------

for dag in dags.values():
    dag.build()

###############################################################################
# Check out the output reports at:
#
# 1. `products/report-setosa.html`
# 2. `products/report-virginica.html`
