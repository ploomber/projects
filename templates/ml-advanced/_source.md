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

ML pipeline using the Python API. Shows how to package project, test it using pytest, and train models in parallel.

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
