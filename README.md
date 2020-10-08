# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/projects/master)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

## Basic examples

1. `spec-api-directory/`. A simple pipeline with 5 tasks, it is executed without declaring a `pipeline.yaml` file. This is the example used in the JupyterCon 2020 demo
2. `spec-api-python/`. Pipeline defined using a `pipeline.yaml` file
3. `spec-api-r/` Basic pipeline with R scripts

## Intermediate examples

4. `spec-api-sql/`
5. `python-api/`. Basic tutorial using the Python API
6. `parametrized/`. Sample parametrized pipeline
7. `debugging/`. Pipeline to demonstrate debugging capabilities
8. `testing/`. Pipeline with SQL and Python tasks showing how test pipelines
9. `ml-basic/`. Simple Machine Learning pipeline using the both APIs (Python and Spec). It also shows how to test pipelines using `pytest` and how to package your pipeline so you can install it with `pip install`

## Advanced examples

10. sql-templating. SQL pipeline showing how to use macros to write concise SQL scripts
11. etl. Pipeline with a dozen tasks demonstrating how to extract data form a SQL database and then process it with Python