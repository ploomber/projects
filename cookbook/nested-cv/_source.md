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

# Nested cross-validation

<!-- start description -->
Nested cross-validation for model selection and hyperparameter tuning.
<!-- end description -->

More details in our [blog.](https://ploomber.io/blog/nested-cv/)

<% expand('pipeline.yaml') %>

Plot:

```sh
# run this in a terminal
ploomber plot
```

```python
# run this in a python session
from IPython.display import Image
Image('pipeline.png')
```

Run the pipeline:

```sh
# run this in a terminal
ploomber build
```