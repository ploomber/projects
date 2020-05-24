import shutil
from pathlib import Path

from ploomber_basic import functions

from ploomber import DAGConfigurator, SourceLoader
from ploomber.tasks import NotebookRunner, PythonCallable
from ploomber.products import File


def make(clean_up=True):
    cfg = DAGConfigurator()
    cfg.params.hot_reload = True
    dag = cfg.create()

    # we will save all output here
    out = Path('output')

    if clean_up and out.exists():
        shutil.rmtree(str(out))

    out.mkdir(exist_ok=True)

    # source loaders allows us to easily load files from modules
    loader = SourceLoader(path='notebooks', module='ploomber_basic')

    # our first task is a Python function, it outputs a csv file
    load = PythonCallable(functions.load,
                          product=File(out / 'data.csv'),
                          dag=dag,
                          name='load')

    # Our second task is a Python script. Since we are using the NotebookRunner
    # task, it will convert it to a Jupyter notebook before execution (you can
    # still pass a .ipynb file). We recommend using .py files as they are
    # easier to merge with git
    clean = NotebookRunner(loader['clean.py'],
                           # this task generates two files, the .ipynb
                           # output notebook and another csv file
                           product={'nb': File(out / 'clean.ipynb'),
                                    'data': File(out / 'clean.csv')},
                           dag=dag,
                           # you can run any language supported by Jupyter
                           # by specifying which kernel to use
                           kernelspec_name='python3',
                           # by enabling this option, a few checks are
                           # performed on your code before running the
                           # notebook. Given that jupyter notebooks are run
                           # cell by cell, something as simple as a syntax
                           # error will be discovered until such cell is run,
                           # this gives you immediate feedback
                           static_analysis=True,
                           papermill_params={'nest_asyncio': True})

    # the final task is also a notebook that generates a plot
    plot = NotebookRunner(loader['plot.py'],
                          File(out / 'plot.ipynb'),
                          dag=dag,
                          kernelspec_name='python3',
                          static_analysis=True,
                          papermill_params={'nest_asyncio': True})

    # declare execution dependencies, by leveraging the graph structure
    # Ploomber can even run tasks in parallel
    load >> clean >> plot

    return dag


if __name__ == '__main__':
    dag = make()
    dag.build()
