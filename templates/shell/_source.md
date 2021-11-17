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

# Executing shell scripts as tasks

*Note: this example requires* `ploomber>=0.13.6`

<!-- start description -->
Create a pipeline with shell scripts as tasks.
<!-- end description -->

## Description

The pipeline has three tasks:

<% expand('pipeline.yaml') %>

We download some data, and plot it with Python. We also have a second
shell script that copies the data from the first one to demonstrate how to
declare upstream dependencies.

## Build pipeline

```bash
ploomber build
```