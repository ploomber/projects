# Ploomber sample projects

![CI](https://github.com/ploomber/projects/workflows/ci/badge.svg)

<p align="center">
  <a href="https://ploomber.io/community">Join our community</a>
  |
  <a href="https://www.getrevue.co/profile/ploomber">Newsletter</a>
  |
  <a href="https://docs.ploomber.io/">Docs</a>
  |
  <a href="https://twitter.com/intent/user?screen_name=ploomber">Twitter</a>
  |
  <a href="https://ploomber.io/">Blog</a>
  |
  <a href="https://www.youtube.com/channel/UCaIS5BMlmeNQE4-Gn0xTDXQ">YouTube</a>
  |
  <a href="mailto:contact@ploomber.io">Contact us</a>
</p>

This repository contains sample pipelines developed using [Ploomber](https://github.com/ploomber/ploomber).

**Note:** We recommend you to go through the [first tutorial](https://docs.ploomber.io/en/latest/get-started/first-pipeline.html) to learn the basics of Ploomber.

## Running examples


Use Colab:

<p align="center">
    <a href="https://colab.research.google.com/github/ploomber/projects/blob/master/guides/first-pipeline/colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

Use Binder (free, hosted JupyterLab):

[![Binder](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster)

Or run locally:

~~~sh
pip install ploomber

# list examples
ploomber examples

# download example with name
ploomber examples --name {name}

# example
ploomber examples --name templates/mlflow
~~~

## How to read the examples

Each example contains a `README.md` file that describes it; a `README.ipynb` is also available with the same contents but in Jupyter notebook format and with command outputs. In addition, files for `pip` (`requirements.txt`) and  `conda` (`environment.yml`) are provided for local execution.

## Index

### Templates

Starting points for common use cases. Use them to ramp up a project quickly.

{% for e in templates %}
{{e.idx}}. [`{{e.path}}`]({{e.path}}/README.ipynb) {{e.description}}
{% endfor %}

### Cookbook

Short and to-the-point examples showing how to use a specific feature.

{% for e in cookbook %}
{{e.idx}}. [`{{e.path}}`]({{e.path}}/README.ipynb) {{e.description}}
{% endfor %}

### Guides

In-depth tutorials for learning.  These are part of the [documentation](https://docs.ploomber.io/en/latest/user-guide/index.html).

{% for e in guides %}
{{e.idx}}. [`{{e.path}}`]({{e.path}}/README.ipynb) {{e.description}}
{% endfor %}


## Python API

The simplest way to get started with Ploomber is via the Spec API, which allows you to describe pipelines using a `pipeline.yaml` file, most examples on this repository use the Spec API. However, if you want more flexibility, you may write pipelines with Python.

The [`templates/python-api/`](templates/python-api) directory contains a project written using the Python API. And the [`python-api-examples/`](python-api-examples) includes some tutorials and more examples.


## Micro-pipelines

In Ploomber `0.21`, we introduced a simplified API to write pipelines in a single Jupyter notebook (or `.py`) file. This is a great option for small projects.

You can find the examples in the [`micro-pipelines/`](micro-pipelines) directory.
