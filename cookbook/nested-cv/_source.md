---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.2
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
ploomber plot
```

Display the pipeline:

```python
from IPython.display import Image
Image('pipeline.png')
# NOTE: ploomber plot will generate a pipeline.html (not .png) file if
# pygraphviz is missing. In such case, open the file to view the pipeline plot
```

Run the pipeline:

```sh
# run this in a terminal
ploomber build
```
