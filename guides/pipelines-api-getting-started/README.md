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

# Cloud Execution

**Note:** To use Ploomber Cloud, you need an API key, [click here](https://docs.ploomber.io/en/latest/cloud/api-key.html) to get one.

Ploomber Cloud allows you to go from your local environment to a distributed environment in the cloud (to run hundreds of experiments in parallel!) and back in a single command.

**Note:** to see a notebook version (with outputs) of this file, [click here.](README.ipynb)

## The pipeline

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

## Setup

We are constantly updating the Ploomber Cloud CLI so ensure you're running the latest version:

```sh
pip install ploomber --upgrade
```

Now, let's set our API key:

```sh
ploomber cloud set-key {your-key}
```

Download this example:

```sh
# download
ploomber examples -n guides/cloud-execution -o example

# move to the example
cd example
```

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
ploomber cloud status 136f9b47-27fa-4f65-b06f-b6fe665f3ea9
```

*Run created...* means Ploomber Cloud is building the Docker image, let's wait a minute to give it some time to finish and send the jobs to the cluster.
Ploomber Cloud runs one container per task, allowing you to parallelize our pipeline easily!
You can check the Docker image building docs with the following command:

```sh
ploomber cloud logs 136f9b47-27fa-4f65-b06f-b6fe665f3ea9 --image
```

It'll take about a minute for the Docker build process to start, you may execute the following command to continuously watch the logs:

```sh
ploomber cloud logs {runid} --image --watch
```

Let's check the status of the individual tasks:

```sh
ploomber cloud status 5fe5d32b-8686-4978-bb26-d11146b576f2
```

Great! We see that our jobs have been scheduled.

You can execute the following to watch the task status continuously:

```sh
ploomber cloud status {runid} --watch
```

Let's give it a few minutes for it to finish training the 10 models, and run the command again:

```sh
ploomber cloud logs 5fe5d32b-8686-4978-bb26-d11146b576f2
```

## Task  logs

To check the logs for each task:

(Note: it may take a few minutes for the task to start, and hence, for the logs to be visible. Ploomber Cloud spins up the necessary infrastructure on-demand, so you only pay for what you use, however, this requires us to shut down any unused infrastructure)
(Note: You can use the latest tag to get the latest run logs: `ploomber cloud logs latest`)

```sh
ploomber cloud logs 136f9b47-27fa-4f65-b06f-b6fe665f3ea9
```

### Or using the latest tag
```sh
ploomber cloud logs latest
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


## Debugging

If any of your notebooks (or scripts) fails, a copy of the partially executed notebook will be uploaded, so you can debug it.

For example, let's say I add the following in my notebook/script:

```python
raise ValueError('some new error!')
```

Upon, execution, I can retrieve the logs with:

```
ploomber cloud logs latest
```
### Or use the runid

```
ploomber cloud logs {runid}
```



And I'll see the following:

```
---------------------------------------------------------------------------
Exception encountered at "In [9]":
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipykernel_41/2195319445.py in <cell line: 1>()
----> 1 raise ValueError('some new error!')
ValueError: some new error!
```

And a few lines below:

```
ploomber.exceptions.TaskBuildError: Error when executing task 'fit'. Partially executed notebook uploaded to remote storage at: products//project/output/nb.ipynb
```

I can download that partially executed notebook with:

```
ploomber cloud download '*nb.ipynb'
```

Then, I can open the notebook, and I'll see the code and cells with their corresponding output so I can debug!

## Abort an executing job

At the moment we do support concurrent executions for paid users only. If you wish to submit a different job while there is one executing in the cloud, you will need to abort the running one using this command:

```
ploomber cloud abort {runid}
```

### Or use the latest tag

```
ploomber cloud abort latest
```

Note: You can use the latest tag to abort the latest run: `ploomber cloud abort latest`
Note: to get the list of runids, execute `ploomber cloud list`

## That's it!

We hope you enjoyed this tutorial and are excited to use Ploomber in your next project. Questions? [Ping us on Slack!](https://ploomber.io/community)
