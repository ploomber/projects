<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/ml-advanced`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/ml-advanced/README.ipynb)
<!-- end header -->



# ML advanced

<!-- start description -->
ML pipeline using the Python API. Shows how to create a Python package, test it with pytest, and train models in parallel.
<!-- end description -->

## Setup

```sh
pip install -r requirements.txt
pip install --editable .
```

## Build

```sh
ploomber build --entry-point ml_advanced.pipeline.make
```

## Testing

```bash
# complete (force execution of all tasks)
pytest --force
```

```bash
# incremental (will only run the tasks that have changed)
pytest
```
