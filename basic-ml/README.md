# Basic ML project


## Installation

```bash
git clone https://github.com/ploomber/basic-pipeline
cd basic-pipeline
pip install .
```

## Executing pipeline

```bash
python -m ploomber.entry basic_pipeline.pipeline.make --help
```

## Testing

```bash
pip install -r requirements.txt

# incremental
pytest

# complete
pytest --force

# to start a debugging session on exceptions
pytest --pdb

# to start a debugging session at the start of every test
pytest --trace
```
