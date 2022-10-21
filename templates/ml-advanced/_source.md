---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

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
