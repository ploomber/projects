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

# Task grids

<!-- start description -->
An example showing how to create a grid of tasks to train models with different parameters.
<!-- end description -->

<% expand('pipeline.yaml', lines=(17, 35)) %>

Run the pipeline:

```sh
ploomber build
```