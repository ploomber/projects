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

# Python API

<!-- start description -->
Loads, clean, and plot data using the Python API.
<!-- end description -->


If you're new to the Python API, check out [python-api-examples/](../../python-api-examples) directory, containing tutorials and more examples.

## Description

This pipeline has three tasks:

1. Load task (Python function): CSV file
2. Clean task (Python script):  Jupyter notebook and another CSV file
3. Plot task (Python scripts): Jupyter notebook

## Setup

```sh
pip install -r requirements.txt
pip install --editable .
```

## Build

```bash
ploomber build
```
