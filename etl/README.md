# ETL example


This example shows a non-trivial pipeline that resembles a typical
scenario when analyzing data. It helps demonstrate how
[Ploomber](https://github.com/ploomber/ploomber) helps you
develop data pipelines without worrying about plumbing code (managing
database connections, orchestrating execution, etc.)

Most notably, this project contains minimal configuration code (just a small
`db.py` file to establish a connection with the database), the rest are scripts
that perform the actual analysis. The `pipeline.yaml` files tells Ploomber how
to run the pipeline and it allows everyone in the analysis team to understand
how all parts stitch together.

This pipeline uses a subset of the [Stack Exchange dataset](https://archive.org/details/stackexchange). It gets the data from the original source, converts it from XML to CSV, uploads it to a database, aggregates it, dumps it and generates a few plots. See the diagram below (generated using `ploomber plot`):

![pipeline](pipeline.png)

The ``pipeline.yaml`` file contains a few comments to understand what's going on at each step.

This project also has non-trivial dependencies: a package to uncompress `.7z` files, a few Python packages, R and the R kernel for Jupyter. Everything is installed via a conda environment. See the `environment.yml` file for details.

On each push, the pipeline is tested, ensuring it works at all times. See `.github/workflows/ci.yml` for details (`etl` job).

## Setup

(Note: Only required if you are running this example in your computer, not
required if using Binder/Deepnote)

~~~bash
# make sure you are in the etl folder.
conda env create --file environment.yml
conda activate etl
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