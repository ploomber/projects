<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/etl`


Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/etl/README.ipynb)
<!-- end header -->




# ETL SQL pipeline

<!-- start description -->
Download a data file, upload it to a database, process it, and plot with Python and R.
<!-- end description -->

**Note:** This pipeline requires the `p7zip` package. It is installed if using `conda` (`environment.yml`). If using `pip`, you must install it yourself.

## Data

Subset of the [Stack Exchange dataset](https://archive.org/details/stackexchange).
It gets the data from the original source, converts it from XML to CSV, uploads it to a database, aggregates it, dumps it and generates a few plots. See the diagram below (generated using `ploomber plot`):

![pipeline](pipeline.png)

The ``pipeline.yaml`` file contains a few comments to understand what's going on at each step.


## Build

```sh
ploomber build
```

Output stored in the ``output/`` directory.
