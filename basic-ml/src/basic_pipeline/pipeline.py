"""
Pipeline declaration using ploomber:

https://github.com/ploomber/ploomber
"""

from pathlib import Path
import tempfile

from ploomber import DAG
from ploomber.tasks import PythonCallable
from ploomber.products import File

from basic_pipeline import tasks


def make(path=None):
    """
    Make pipeline

    Parameters
    ----------
    path : str
        Output path

    Returns
    -------
    ploomber.DAG
        A pipeline object

    Notes
    -----
    This is a numpy docstring, which is the standard format in the Python data
    ecosystem: https://numpydoc.readthedocs.io/en/latest/format.html
    """

    if path is None:
        path = Path(tempfile.mkdtemp())

    dag = DAG()

    get = PythonCallable(tasks.get,
                         File(path / 'data.parquet'),
                         dag,
                         name='get')

    fts = PythonCallable(tasks.features,
                         File(path / 'features.parquet'),
                         dag,
                         name='features')
    join = PythonCallable(tasks.join,
                          File(path / 'join.parquet'),
                          dag,
                          name='join')

    fit = PythonCallable(tasks.fit, {'report': File(path / 'report.txt'),
                                     'model': File(path / 'model.joblib')},
                         dag,
                         name='fit')

    get >> fts

    (get + fts) >> join

    join >> fit

    return dag
