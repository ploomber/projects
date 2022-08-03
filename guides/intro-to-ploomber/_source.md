---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


# Your first Python pipeline

<!-- start description -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n guides/first-pipeline`

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=guides/first-pipeline%20issue) Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)
<!-- end description -->

# Ploomber Tutorial Intro

- This should showcase the Ploomber value proposition. 
- We'll do a few ML operations in a notebook, using a sample covid-19 dataset. 
- We'll forcast the relation between testing and active covid cases.

**For a deeper dive**, try the [first-pipeline guide](https://docs.ploomber.io/en/latest/get-started/first-pipeline.html). 

If YAML, Jupyter and notebooks sounds like a distant cousin, please check our [basic concepts guide](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).

### We'll see today how you can improve your work:
- Run 100s of notebooks in parallel 
- Parameterize your workflows
- Easily generate HTML/PDF reports


# Parallelization

- Ploomber creates a pipeline for you, so you can run independent tasks simultanously. 

- It also cache some results so you don't have to wait. You can drop the `force=True` (last line) and rerun this cell.

In here we'll train 4 different models simultanously, and see it in a graph:

```python
from ploomber import DAG
from ploomber.tasks import ShellScript, PythonCallable
from ploomber.products import File
from ploomber.executors import Serial

from ploomber.spec import DAGSpec
spec = DAGSpec('./pipeline.yaml')
dag = spec.to_dag()
status = dag.status()
_ = dag.build(force=True)
```

```python
dag.plot()
```

# Parameterize workflows
- We're using our linear-regression and passing a bool flag to intercept (True/False)
- We can take the best results by parameterizing our workflow to fit different variations

```python
from ploomber.spec import DAGSpec
spec = DAGSpec('./pipeline-parameterization.yaml')
dag = spec.to_dag()
status = dag.status()
_ = dag.build(force=True)
```

```python
dag.plot()
```

# Automated reports

In case we have a dataset to track or a stakeholder report, we can generate it as part of our workflow.
Here we'll create a HTML report for our business persona from our previous linear regression task:

```python
# open each specific html report/data
from IPython.display import IFrame
IFrame(src="./output/linear-regression.html", width='100%', height='500px')
```

# Where to go from here

### Usecases
Read how you can leverage this tool to [benefit your needs](https://docs.ploomber.io/en/latest/use-cases/index.html)

### Community suport
Have questions? [Ask us anything on Slack](https://ploomber.io/community/).

### Resources
**Bring your own code!** Check out the tutorial to [migrate your code to Ploomber](https://docs.ploomber.io/en/latest/user-guide/refactoring.html).


Want to dig deeper into Ploomber's core concepts? Check out [the basic concepts tutorial](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).

Want to start a new project quickly? Check out [how to get examples](https://docs.ploomber.io/en/latest/user-guide/templates.html).
