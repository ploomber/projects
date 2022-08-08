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
Introductory tutorial to learn the basics of Ploomber.
<!-- end description -->

# Ploomber Tutorial Intro

We'll forcast the relation between testing and active covid-19 cases. 

### We'll see today how you can improve your work:
- Run 100s of notebooks in parallel 
- Parameterize your workflows
- Easily generate HTML/PDF reports


**For a deeper dive**, try the [first-pipeline guide](https://docs.ploomber.io/en/latest/get-started/first-pipeline.html) or the [basic concepts overview](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).
If YAML, Jupyter and notebooks sounds like a distant cousin, please check our [basic concepts guide](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).


# Parallelization

- Ploomber creates a pipeline for you, so you can run independent tasks simultaneously. 

- It also cache the results so you don't have to wait. You can drop the `force=True` (last line) and rerun this cell.

In here we'll train 4 different models simultaneously, and see it in a graph:

```python
from ploomber import DAG
from ploomber.tasks import ShellScript, PythonCallable
from ploomber.products import File
from ploomber.executors import Parallel

from ploomber.spec import DAGSpec
spec = DAGSpec('./pipeline.yaml')
dag = spec.to_dag()
dag.executor = Parallel()
_ = dag.build(force=True)
```

```python
dag.plot()
```

# Parameterize workflows
- In many cases, you'd run your analysis with different parameters/different data slices
- Ploomber allows you to parametrize workflows easily
- Here we're training a linear regression with different parameters, using a notebook as template

```python
from ploomber.spec import DAGSpec
spec = DAGSpec('./pipeline-parameterization.yaml')
dag = spec.to_dag()
dag.plot()
```

```python
_ = dag.build(force=True)
```

# Automated reports

In case we have a dataset to track/a stakeholder report, we can generate it as part of our workflow.
We created the report as part of our first cell pipeline build, so we can consume it immediately.
Let's load our stakeholder report from our previous linear regression task:

```python
# open each specific html report/data if exist
from IPython.display import IFrame
from pathlib import Path

report = "./output/linear-regression.html"
if Path(report).is_file():
    IFrame(src=report, width='100%', height='500px')
else:
    print("Report doesn't exist - please run the notebook sequentially")
```

# Where to go from here

### Use cases

- [Machine Learning](https://docs.ploomber.io/en/latest/use-cases/ml.html)
- [Research Projects](https://docs.ploomber.io/en/latest/use-cases/research.html)
- [Analytics](https://docs.ploomber.io/en/latest/use-cases/analytics.html)
- [SQL Pipelines](https://docs.ploomber.io/en/latest/use-cases/sql.html)

### Community support
Have questions? [Ask us anything on Slack](https://ploomber.io/community/).

### Resources
**Bring your own code!** Check out the tutorial to [migrate your code to Ploomber](https://docs.ploomber.io/en/latest/user-guide/refactoring.html).


Want to dig deeper into Ploomber's core concepts? Check out [the basic concepts tutorial](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).

Want to start a new project quickly? Check out [how to get examples](https://docs.ploomber.io/en/latest/user-guide/templates.html).
