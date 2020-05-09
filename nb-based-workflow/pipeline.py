"""
Launch an interactive session:

To run:
"""
from pathlib import Path

from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File


# Small notebooks are easier to debug and manage than a big monolithic one
# It is hard to make diffs on .ipynb files (they are JSON strings), this
# makes pull requests complicated, we use regular .py files that are
# converted on demand to notebooks instead. We can also exploit the
# dependency structure to run things in parallel

# TODO: enable hot_reload

dag = DAG(executor='parallel')

# Our notebook declaration is minimal, we just specify where the soruce code
# is located and where to save the executed notebooks and any other files
# the notebook will save
out = Path('output')
out.mkdir(exist_ok=True)
nb = Path('notebooks')

# avoid hardcoding paths to files, instead, add them during execution,
# this makes easy to switch folders (e.g. for a different developer storing
# results in a different location).

# static analysis prevents notebooks with errors from being executed, saving
# us time if the notebook performs long-running computations

# notebooks do not have to be in Python, they can be in R, Julia or any
# other language supported by Jupyter
load = NotebookRunner(nb / 'load.py',
                      product={'nb': File(out / 'load.ipynb'),
                               'data': File(out / 'data.csv')},
                      dag=dag,
                      kernelspec_name='python3',
                      static_analysis=True)


clean = NotebookRunner(nb / 'clean.py',
                       product={'nb': File(out / 'clean.ipynb'),
                                'data': File(out / 'clean.csv')},
                       dag=dag,
                       kernelspec_name='python3',
                       static_analysis=True)


plot = NotebookRunner(nb / 'plot.py',
                      File(out / 'plot.ipynb'),
                      dag=dag,
                      kernelspec_name='python3',
                      static_analysis=True)

# declare execution dependencies
load >> clean >> plot

# render workflow, inject cells with parameters (product, upstream)
# and make sure all looks good before execution
dag.render()

# plot workflow
dag.plot()

# generate a summary report - useful to given a high-level overview for new
# developers and stakeholders
_ = dag.to_markup(path=out / 'report.html')


# build workflow
dag.build()

# we can edit the .py source code files directly but there is a nicer way.
# since our tasks have dependencies, they need access to them to run, (e.g.
# the plot task needs access to the path where the clean data is stored),
# task.debug() will create a temporary notebook with such parameters added as
# a new cell, such cell is removed before saving the notebook
clean.debug()

# build again, only notebooks whose source code has changed will be executed
dag.build()

# Fully reproducible: delete files, move code around and try again

