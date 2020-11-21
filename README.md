# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

## Starting an interactive environment

If you want to play around with the examples without installing anything, you
have two options Binder or Deepnote. The main difference is that Deepnote
requires you to have a free account (you can quickly do so if you have a Github
account), but it loads much faster (although not all examples work there yet).

[<img src="https://deepnote.com/buttons/launch-in-deepnote.svg">](https://deepnote.com/launch?template=deepnote&url=https://github.com/ploomber/projects/blob/master/README.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/projects/master)


## How to read the examples

Each example contains a `README.md` file with more information, and a
`README.ipynb` file which has the same contents as the `.md` file but in a
Jupyter notebook format and with the output from each cell.

## Where to start?

* Simplest example: [`spec-api-directory/`](spec-api-directory/README.ipynb)
* Machine Learning example: [`ml-basic/`](ml-basic/README.ipynb)
* SQL ETL example: [`spec-api-sql/`](spec-api-sql/README.ipynb)

## Index

### Basic

1. `spec-api-directory/` Simple example showing how to build a pipeline out of a directory with scripts. This is the example used in the JupyterCon 2020 demo
2. `spec-api-python/` Python pipeline defined using a `pipeline.yaml` spec file
3. `spec-api-r/` R pipeline defined using a `pipeline.yaml` spec file
4. `ml-basic/` Basic Machine Learning pipeline with a few function tasks and a notebook task for training a model

### Intermediate

5. `spec-api-sql/` Pipeline with SQL and Python tasks, using the Spec API
6. `python-api/` Pipeline using the Python API
7. `parametrized/` Pipeline with input parameters
8. `debugging/` Pipeline to demonstrate debugging capabilities
9. `testing/` Pipeline with SQL and Python tasks showing how to test pipelines
10. `ml-intermediate/` ML pipeline (Spec API). Similar to `ml-basic/` but shows how to do integration testing using `on_finish` and speed testing up by parametrizing the pipeline with a sample on/off option, switched via command line

### Advanced

10. `sql-templating` SQL pipeline showing how to use macros to write concise SQL scripts
11. `etl` Pipeline with a SQL tasks demonstrating how to extract data from a database and then process it with Python and R
12. `ml-advanced/` Machine Learning pipeline using the Python API, how to package
your projects so you can install them using `pip install .`, how to test
using `pytest`, how to create an array of experiments to try several models and
run them in parallel.
