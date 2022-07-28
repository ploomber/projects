"""
Example showing how to run all notebooks in a directory
"""
from pathlib import Path
from glob import glob

from ploomber.tasks import NotebookRunner
from ploomber.executors import Parallel
from ploomber.products import File
from ploomber import DAG


def get_dag():
    base_dir = Path(__file__).parent
    # NOTE: recursive needed if there are notebooks in nested directories
    paths = glob(str(base_dir / 'notebooks/**/*.ipynb'), recursive=True)
    paths_print = ' '.join(f'\n - {path}' for path in paths)

    print(f'Notebooks:{paths_print}')

    dag = DAG(executor=Parallel(processes=4))

    # NOTE: notebook files must have a cell with the "parameters" tag
    # see: https://ploomber.io/s/params
    for path in paths:
        basename = Path(path).name
        NotebookRunner(Path(path),
                       File(Path(base_dir, 'output', basename)),
                       dag=dag)

    return dag


if __name__ == '__main__':
    dag = get_dag()
    # this will only run notebooks that have changed, to force execution,
    # pass force=True. Note that the changes are tracked via the .metadata
    # files in the output folder
    dag.build()
