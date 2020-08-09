# ETL example


This example shows a non-trivial pipeline that resembles a typical
scenario when analyzing data. It helps demonstrate how you can develop pipelines without worrying about plumbing code and focus on the analysis.

This pipeline uses a subset of the [Stack Exchange dataset](https://archive.org/details/stackexchange). It gets the data from the original source, converts it
to CSV, uploads it to a database, aggregates it, dumps it and
generates a few plots. See the diagram below (generated using `ploomber plot`):

![pipeline](pipeline.png)

The ``pipeline.yaml`` file contains a few comments to understand what's going
on at each step.

This project also has non-trivial dependencies: a package to uncompress `.7z`
files, a few Python packages, R and the R kernel for Jupyter. Everything is installed via a conda environment. See the `environment.yml` file for details.

On each push, the pipeline is tested, ensuring it works at all times. See `.github/workflows/ci.yml` for details (`etl` job).

