# Basic ML project

This example shows how to build a Machine Learning pipeline using the Spec API.

You can run this from your computer (Jupyter or terminal), or use one of the
hosted options: deepnote (requires free account but loads faster) or binder.

| [![deepnote-logo](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?template=deepnote&url=https://github.com/ploomber/projects/blob/master/ml-basic/README.ipynb) | [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/projects/master?urlpath=%2Flab%2Ftree%2Fml-basic%2FREADME.ipynb) |
|---|---|


## Setup (skip if using deepnote or binder)

(**Note**: Only required if you are running this example in your computer, not
required if using Binder/Deepnote)

~~~bash
# make sure you are in the ml-basic folder.
conda env create --file environment.yml
conda activate ml-basic
~~~

## Description

Let's take a look at the `pipeline.yaml file`:

```bash tags=["bash"]
cat pipeline.yaml
```

Note that we changed one of the default settings: instead of
extracting the output directly from the source code, we'll declare it in
the `pipeline.yaml` file. Also observe that the first three tasks as Python
functions, while the last one is a script.

Generate the plot:

```bash tags=["bash"]
# Note: plotting doesn't work in deepnote
ploomber plot
```

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

This pipeline gets some data, generates some features and trains a model.

## Executing the pipeline from the command line (shell)

```bash tags=["bash"]
ploomber build
```

Since the training task is a script, it will generate a jupyter notebook,
[open it](output/nb.ipynb) to see the generated evaluation charts.

## Interacting with your pipeline from Python session

The shell command line interface is a convenient way to interact with your
pipeline. You can also load your pipeline in a Python session, which offers
more features than the shell version.

To load a pipeline from a `pipeline.yaml` file:

```python
from ploomber.spec import DAGSpec
dag = DAGSpec('pipeline.yaml').to_dag()

# same as "ploomber status"
dag.status()
```

```python
# same as "ploomber build"
dag.build()
```

``DAG`` has a dict-like interface, to get a task:

```python
dag['fit']
```

There are a lot of things you can do with from a Python session, see the
documentation for ``ploomber.DAG`` for details.

A shortcut to initialize a Python session from a terminal:

~~~bash
ploomber interact
~~~

## Where to go from here

* [`ml-intermediate/`](../ml-intermediate/README.ipynb) contains another ML
pipeline with more features. It shows how to parametrize a pipeline using
an `env.yaml` file (so you can run your pipeline with a small sample to test things quickly), run integration tests using `on_finish` and customizing output notebooks/reports.