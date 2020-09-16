# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/projects/master)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

## Basic examples

1. entry-directory. A simple pipeline with 5 tasks, it is executed without declaring a `pipeline.yaml` file. This is the example used in the JupyterCon 2020 demo
2. spec-basic. Pipeline defined using a `pipeline.yaml` file
3. spec-r. Basic pipeline with R scripts

## Intermediate examples

1. parametrized. Sample parametrized pipeline
2. debugging. Pipeline to demonstrate debugging capabilities
3. sql-templating. SQL pipeline showing how to use macros to write concise SQL scripts
4. testing. Pipeline with SQL and Python tasks showing how to add test pipelines

## Advanced examples

1. etl. Pipeline with a dozen tasks demonstrating how to extract data form a SQL database and then process it with Python