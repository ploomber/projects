# ML advanced

This example shows a Machine Learning pipeline using the Python API, how to package
your projects so you can install them using `pip install .`, how to test
using `pytest`,how to create an array of experiments to try several models and
run them in parallel.

## Setup

Make sure you are in the `ml-advanced` folder:

~~~bash
# if using conda
conda env create --file environment.yml
conda activate ml-advanced

# otherwise use pip directly
pip install -r requirements.txt

# install the pipeline as a package in editable mode
pip install --editable .
~~~

## Executing pipeline

```bash tags=["bash"]
ploomber build --entry-point ml_advanced.pipeline.make
```

## Deploy to airflow

WIP

```bash
```


## Testing

~~~bash
# incremental (will only run the tasks that have changed)
pytest

# complete (force execution of all tasks)
pytest --force

# to start a debugging session on exceptions
pytest --pdb

# to start a debugging session at the start of every test
pytest --trace
~~~

## Interacting with the pipeline

In a Python session (make sure `ml-advanced/env.yaml` is in the current active
directory):


```python
from ml_advanced.pipeline import make

dag = make()
dag.status()
```
