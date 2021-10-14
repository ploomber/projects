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

# Dynamic params

<!-- start description -->
Pipeline parameters whose values are computed at runtime.
<!-- end description -->

Run the pipeline:

```sh
python run.py
```

Check output (stored in directory with name `0`):

```sh
ls products
```

Run again:

```sh
python run.py
```

Check output (this time, stored in directory with name `1`):

```sh
ls products
```