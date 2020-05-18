from pathlib import Path

from ploomber_nb import functions

from ploomber import DAGConfigurator, SourceLoader
from ploomber.tasks import NotebookRunner, PythonCallable
from ploomber.products import File


def make():
    cfg = DAGConfigurator()
    cfg.params.hot_reload = True
    dag = cfg.create()

    # we will save all output here
    out = Path('output')
    out.mkdir(exist_ok=True)

    # source loaders allows us to easily load files from modules
    loader = SourceLoader(path='notebooks', module='ploomber_nb')

    # out first task is a Python function, it generates and output csv file
    load = PythonCallable(functions.load,
                          product=File(out / 'data.csv'),
                          dag=dag,
                          name='load')

    # Our second task is a Python script, why is it using a task called
    # NotebookRunner? This task runs code as a Jupyter notebook, you might
    # pass a .ipynb but you can pass .py files as well, which will be converted
    # to notebooks before execution. It is hard to run git diff .ipynb files
    # (they are JSON strings), using scripts allows you to easily control
    # versions
    clean = NotebookRunner(loader['clean.py'],
                           # this task generates two files, the .ipynb
                           # output notebook itself and another csv file
                           product={'nb': File(out / 'clean.ipynb'),
                                    'data': File(out / 'clean.csv')},
                           dag=dag,
                           # you can run any language supported by Jupyter
                           # by specifying which kernel to use
                           kernelspec_name='python3',
                           # by enabling this option, a few checks are
                           # performed on your code before running the
                           # notebook, given that jupyter notebooks are run
                           # cell by cell, something as simple as a syntax
                           # error will be discovered until such cell is run
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
