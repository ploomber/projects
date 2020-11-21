# Basic ML project

This example shows how to build a Machine Learning pipeline using the Spec API.

Take a look at the `pipeline.yaml` for more details.

## Setup

(Note: Only required if you are running this example in your computer, not
required if using Binder/Deepnote)

~~~bash
# make sure you are in the ml-basic folder.
conda env create --file environment.yml
conda activate ml-basic
~~~

## Pipeline summary

```bash tags=["bash"]
ploomber status
```

## Executing the pipeline from the command line (shell)

```bash tags=["bash"]
ploomber build
```

Output is generated in the ``output/`` directory.

## Interacting with your pipeline from Python session

```python
from ploomber.spec import DAGSpec

dag = DAGSpec('pipeline.yaml').to_dag()
dag.status()
```

```python
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

`ml-intermediate` contains another ML pipeline with more features. It shows how
to parametrize a pipeline using an `env.yaml` file (so you can run your pipeline
with a small sample to test things quickly), run integration tests using
`on_finish` and customizing output notebooks/reports.