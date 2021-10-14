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

# R pipeline

<!-- start description -->
Load, clean and plot data with R.
<!-- end description -->

**Note:** If using conda (`environment.yml`), R will be installed and configured. If using pip (`requirements.txt`), you must install R and [configure it yourself]( https://github.com/IRkernel/IRkernel).


## Pipeline description

This pipeline contains three tasks. The last task generates a plot. To get the
pipeline description:

```bash
ploomber status
```

## Build the pipeline from the command line

```bash
mkdir output
ploomber build
```

Output stored in the ``output/`` directory.
