# Basic ML project

This example shows a simple ML pipeline using the Python API, how to package
your projects so you can install them using `pip install .` and how to test
using `pytest`.

The same pipeline was implemented using the Spec API using the source code
from this example to show a comparison between the Spec and Python API, see `spec/` for details.

## Setup

```bash
git clone https://github.com/ploomber/projects
cd basic-ml
pip install .
```

## Executing pipeline

```bash
ploomber build --entry-point basic_ml.pipeline.make
```

## Testing

```bash
pip install -r requirements.txt

# incremental (will only run the tasks that have changed)
pytest

# complete (force execution of all tasks)
pytest --force

# to start a debugging session on exceptions
pytest --pdb

# to start a debugging session at the start of every test
pytest --trace
```

## Interacting with the pipeline

In a Python session (make sure `basic-ml/env.yaml` is in the current active
directory):

```python
from basic_ml.pipeline import make

dag = make()
```
