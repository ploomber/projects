# ML advanced

ML pipeline using the Python API. Shows how to package project, test it using pytest and train models in parallel.

## Setup

(**Note**: Skip if running in binder or deepnote)

~~~bash
# if using conda
conda env create --file environment.yml
conda activate ml-advanced

# otherwise use pip directly
pip install -r requirements.txt
# install the pipeline as a package in editable mode
pip install --editable .
~~~

## Build

```bash tags=["bash"]
ploomber build --entry-point ml_advanced.pipeline.make
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
