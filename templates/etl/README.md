<!-- start header -->
To run this example locally, execute: `ploomber examples -n etl`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fetl%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=etl%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/etl/README.ipynb)
<!-- end header -->




# ETL SQL pipeline

SQL pipeline that downloads data, uploads to a database, process it, and plots using Python/R

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