# ETL SQL pipeline

SQL pipeline that downloads data, uploads to a database, process it, and plots using Python/R

## Data

Subset of the [Stack Exchange dataset](https://archive.org/details/stackexchange).
It gets the data from the original source, converts it from XML to CSV, uploads it to a database, aggregates it, dumps it and generates a few plots. See the diagram below (generated using `ploomber plot`):

![pipeline](pipeline.png)

The ``pipeline.yaml`` file contains a few comments to understand what's going on at each step.

## Setup

(**Note**: Skip if running in binder or deepnote)

~~~bash
# make sure you are in the etl folder.
conda env create --file environment.yml
conda activate etl

# or use pip directly
pip install -r requirements.txt
~~~

**Note:** This pipeline requires the `p7zip` package. It is installed if using
`conda`. If using `pip`, you must install it manually.


## Build

```bash tags=["bash"]
ploomber build
```

Output stored in the ``output/`` directory.