# Data Science sample project

# TODO: add travis.yml

This is a sample project to suggest how a Data Science project could be organized as well as propose some good practices.

## Overview

A lot of Data Science projects contain the following steps:

1. Data loading: download raw data, clean it and load it to a database
2. Exploratory data analysis: explore the data to understand it
3. Feature engineering: process your data to make it suitable for modeling
4. Modeling: fit your models
5. Evaluation: evaluate your models

The motivation for this template is to reflect those steps.

## Folder structure

* `load/` - code for data loading
* `explore/` - notebooks with exploratory data analysis
* `transform/` - code for building features
* `train/` - code for training models
* `evaluate/` - code for evaluating models

There are two more folders:

* `package/` - a Python package with code used across the project
* `tests/` - code and data tests

## Running the pipeline

```shell
git clone https://github.com/edublancas/ds-template
cd ds-template

# optional: configure env.yaml

# install package and all dependencies
pip install src/

# verify all is installed correctly and you are able to instantiate the
# pipeline
pytest

# run the pipeline
python run.py
```

## Exploring output

check notebooks

pipeline declaration in pipeline/pipeline

tasks in */tasks.py



