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

Sample code for creating task grids, this example uses `grid` to create many tasks at once:

<% expand('pipeline.yaml', lines=(17, 35)) %>

Run the pipeline:

```sh
ploomber build
```