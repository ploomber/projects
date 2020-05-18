"""
Start session:

ipython -i -m ploomber.entry pipeline.make status

"""

from pipeline import make

dag = make()

dag.plot()

# build workflow
dag.build()

# plot updated
dag.plot()

# we can edit the .py source code files directly but there is a nicer way.
# since our tasks have dependencies, they need access to them to run, (e.g.
# the plot task needs access to the path where the clean data is stored),
# task.debug() will create a temporary notebook with such parameters added as
# a new cell, such cell is removed before saving the notebook
dag['clean'].debug()

# plot updated
dag.plot()

# build again, only notebooks whose source code has changed will be executed
# static analysis is run on each notbeook before execution
dag.build()
