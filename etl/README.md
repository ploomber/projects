# ETL example


This example shows a non-trivial pipeline that resembles a typical
scenario when analyzing data. It helps demonstrate how Ploomber helps you
develop data pipelines without worrying about plumbing code (managing
database connections, orchestrating execution, etc.)

Most notably, this project contains minimal configuration code (just a small
`db.py` file to establish a connection with the database), the rest are scripts
that perform the actual analysis. The `pipeline.yaml` files tells Ploomber how
to run the pipeline and it allows everyone in the analysis team to understand
how all parts stitch together.

This pipeline uses a subset of the [Stack Exchange dataset](https://archive.org/details/stackexchange). It gets the data from the original source, converts it
from XML to CSV, uploads it to a database, aggregates it, dumps it and
generates a few plots. See the diagram below (generated using `ploomber plot`):

![pipeline](pipeline.png)

The ``pipeline.yaml`` file contains a few comments to understand what's going
on at each step.

This project also has non-trivial dependencies: a package to uncompress `.7z`
files, a few Python packages, R and the R kernel for Jupyter. Everything is installed via a conda environment. See the `environment.yml` file for details.

On each push, the pipeline is tested, ensuring it works at all times. See `.github/workflows/ci.yml` for details (`etl` job).

## Build the pipeline

```sh
# clone repo
git clone https://github.com/ploomber/projects

# move to this folder
cd projects/etl

# install dependencies
conda env create --file environment.yml
conda activate etl

# build (takes a couple minutes to finish)
ploomber build
```

All output is saved in the `output/` directory.