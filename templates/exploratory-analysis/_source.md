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

# Exploratory Data Analysis

<!-- start description -->
Sample pipeline that explores penguins data.
<!-- end description -->

It contains five tasks, to get, clean, and visualize the data:

<% expand('pipeline.yaml') %>

Generate the plot (note that this requires `pygraphviz`, you can skip this if you want):

<!-- #md -->
```sh
ploomber plot
```
<!-- #endmd -->


Open the `pipeline.png` file to see the diagram.

## Build pipeline

```sh
ploomber build
```

Each task generates an HTML report, go to the `products/` directory after
building the pipeline to see them.