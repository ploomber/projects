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

# Hooks

<!-- start description -->
Task hooks
<!-- end description -->

Run the pipeline:

```sh
ploomber build
```

Crash the pipeline (to see how on_failure hooks work):

<!-- #md -->

```sh
ploomber build --env--crash true
```

<!-- #endmd -->