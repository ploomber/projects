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

# Loading pipeline.yaml in Python

<!-- start description -->
Load pipeline.yaml file in a Python session to customize initialization.
<!-- end description -->

## Loading the pipeline

Create a function that loads it and returns the DAG object:

<% expand('pipeline.py') %>

*Note:* If your pipeline isn't using an `env.yaml` file, remove the decorator and the `env` argument in the function.


## Command-line interface

The CLI will work just as if you were using the `pipeline.yaml` file directly, pass the dotted path to the function in the `--entry-point/-e` argument:

```sh
ploomber status -e pipeline.make
```

To build the pipeline:

```sh
ploomber build -e pipeline.make
```

Note that you can modify values set in the `env.yaml`, to see how, pass ``--help``:

```sh
ploomber build -e pipeline.make --help
```

*Note:* Check out the other functions in `pipeline.yaml` for more examples.