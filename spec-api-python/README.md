# Your first Python pipeline

This tutorial will guide you to run your first pipeline with Ploomber. You can either use a terminal from your computer, deepnote (requires free account
but loads faster) or binder.

| ![https://deepnote.com/launch?template=deepnote&url=https://github.com/ploomber/projects/blob/master/README.ipynb](https://deepnote.com/buttons/launch-in-deepnote-small.svg) | ![https://mybinder.org/v2/gh/ploomber/projects/master?filepath=workspace%2FREADME.md](https://mybinder.org/badge_logo.svg) |
|---|---|

*Note:* you can follow this tutorial either from a terminal or an
IPython/Jupyter session. If using the terminal, just remove the `%%sh`, this is just a IPython/Jupyter feature to run shell commands, same as running the command from a terminal.

## Setup (if running locally, skip if using deepnote or binder)

Get code (run in a terminal):

~~~sh
git clone https://github.com/ploomber/projects
ce projects/spec-api-python
~~~

Install dependencies:

~~~sh
conda env create --file environment.yaml
conda activate spec-api-python
~~~

## Description

This pipeline contains 3 tasks. Let's visualize it:

*Note*: plotting is not supported in deepnote.

```bash tags=["bash"]
ploomber plot
```

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

To get the pipeline description:

```bash tags=["bash"]
ploomber status
```

Dependencies are declared inside each script. Take a look a the three Python scripts to check out dependencies declared in in the ``upstream`` variable.
You should see that those dependencies match the diagram above.

*Note: *Each task in the pipeline is a Python script, but you can also use notebooks as tasks.

## Build the pipeline from the command line

```bash tags=["bash"]
mkdir output
ploomber build
```

If you go back to the file list you'll see that `output/` is no longer
empty. Each script was converted to a notebook and executed, you'll also see a
few data files.


```bash tags=["bash"]
ls output/
```

## Updating the pipeline

Quick experimentation is essential to develop data pipeline. Ploomber allows
you to quickly run new experiments without having to keep track of tasks
dependencies.

Let's say you found a problematic column in the data and want to add more
cleaning logic to your `clean.py` script. `raw.py` does not depend
on `clean.py` (it's actually the other way around), but `plot.py` does.

If you modify `clean.py`, you'd have to execute `clean.py` and
then `plot.py` to bring your pipeline up-to-date.

As your pipeline grows in number of tasks keeping track of task dependencies
isn't fun. Automatic dependency tracking guarantees that your tasks are using
the right inputs without having to re-compute the whole thing again.

Make some changes to the `clean.py` script, then build again:

```bash tags=["bash"]
ploomber build
```


You'll see that `raw.py` didn't run because it was not affected by the change!


## Where to go from here

* The next tutorial explains Ploomber's (:doc:`../get-started/basic-concepts`)

The `pipeline.yaml` file is optional, for an example pipeline without it
[click here](../spec-api-directory/README.ipynb). However, it gives you more
flexibility, if you want to see a more complete example, take a look at
[`ml-basic/`](../ml-basic/README.ipynb), which builds a simple Machine
Learning pipeline where some of the tasks are Python functions (instead of scripts).

[`spec-api-sql/`](../spec-api-sql/README.ipynb) contains an example where data manipulation starts in a SQL
database, the data is downloaded and visualized using Python.

Using a `pipeline.yaml` file is a convenient way to write your workflows and is
often enough for a lot of projects. However, if you need more flexibility, you
can use the Python API directly, see the [`python-api/`](../python-api/README.ipynb) example.

If you use R, take a look a the [`spec-api-r/`](../spec-api-r/README.ipynb) example, which contains a similar
pipeline to this but using R.
