# Python API

Pipeline using the Python API

## Setup

~~~bash
# if using conda
conda env create --file environment.yml
conda activate python-api

# otherwise use pip directly
pip install -r requirements.txt
# install the pipeline as a package in editable mode
pip install --editable .
~~~

## Description

This pipeline has three tasks:

1. Load task (Python function): CSV file
2. Clean task (Python script):  Jupyter notebook and another CSV file
3. Plot task (Python scripts): Jupyter notebook

## Build

```bash tags=["bash"]
ploomber build
```
