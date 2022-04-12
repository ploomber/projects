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

# Cloud execution

**Note:** Ploomber Cloud execution is currently in private alpha. If you'd like try it out. [Join our community](https://ploomber.io/community) and ask us for an invite.

Ploomber Cloud allows you to go from your local environment to a distributed environment in the cloud (to run hundreds of experiments in parallel!) and back in a single command.

**Note:** to see a notebook version (with outputs) of this file, [click here.](README.ipynb)

## Setting up

We'll run a sample pipeline that prepares some data and trains 10 models in parallel, here's how the pipeline looks like:

```python
from ploomber.spec import DAGSpec
```

```python
dag = DAGSpec('pipeline.yaml').to_dag()
dag.plot()
```

All we need is to provide a `requirements.lock.txt` with the dependencies that our project needs. No need to learn Kubernetes! Ploomber Cloud will to all the heavy lifting of sending our code to the cloud, creating a Docker image, scheduling jobs, communicating them and storing the results.

<!-- #region -->
## To the cloud!

In Ploomber, you run pipelines with:

```sh
ploomber build
```

To run the pipeline in the cloud, you do:

```sh
ploomber cloud build
```

Let's see it in action!
<!-- #endregion -->

```sh
ploomber cloud build
```

That's it! Let's now check that our pipeline was scheduled:

```sh
ploomber cloud list
```

We can see our runs in the list, let's copy the ID to retrieve the status:

```sh
ploomber cloud status 5fe5d32b-8686-4978-bb26-d11146b576f2
```

*Run created...* means Ploomber Cloud is building the Docker image, let's wait a minute to give it some time to finish and send the jobs to the cluster...

```sh
ploomber cloud status 5fe5d32b-8686-4978-bb26-d11146b576f2
```

Great! We see that our jobs have been scheduled, let's give it a few minutes for it to finish training the 10 models.

```sh
ploomber cloud status 5fe5d32b-8686-4978-bb26-d11146b576f2
```

Let's review the logs:

```sh
ploomber cloud logs 5fe5d32b-8686-4978-bb26-d11146b576f2
```

## ...and back!

Great, so our jobs have finished. We can explore our cloud storage to see what files are available:

```sh
ploomber cloud products
```

Each model training task automatically generates an HTML report, let's download them all:

```sh
ploomber cloud download '*.html'
```

Each `fit` task generated a model evaluation report. Go check them out!


## Incremental builds

Ploomber allows you to dramatically speed up iterations with incremental builds. Let's revisit our pipeline structure:

```python
dag.plot()
```

Let's say you modify the `join` task. If you run `ploomber cloud build`, Ploomber Cloud will only execute the tasks that have changed. So it will run `join`, and all the `fit` tasks, but skip `get`, and `features`!

To force execution of all tasks, you may execute:  `ploomber cloud build --force`


## That's it!

We hope you enjoyed this tutorial and are excited to use Ploomber in your next project. Questions? [Ping us on Slack!](https://ploomber.io/community)
