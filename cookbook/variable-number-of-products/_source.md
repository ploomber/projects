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

# Tasks with a variable number of products

<!-- start description -->
Shows how to create tasks whose number of products depends on runtime conditions.
<!-- end description -->

1. [Basic](basic) - Basic example
2. [Serializer](serializer) - Example using serializer and unserializer


```sh
cd basic
ploomber build --entry-point pipeline.yaml
```

```sh
cd serializer
ploomber build --entry-point pipeline.yaml
```