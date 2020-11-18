# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/projects/master)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

Each example contains a `README.md` file with more information, and a
`README.ipynb` file which has the same contents as the `.md` file but it also
contains the commands output.

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
