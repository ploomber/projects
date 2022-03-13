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

## Get a sample pipeline

<!-- start description -->
To show the capabilities we'll run our pipeline monitoring through a pre-built Ploomber template: ml-basic.
<!-- end description -->

```bash
ploomber plot
```

```python
# If using jupyter, you can show the plot with this code:
from IPython.display import Image
Image(filename='pipeline.png')

# otherwise open the pipeline.png file directly
```

Let's take a look at the `pipeline.yaml`:

<% expand('pipeline.yaml') %>


## Setup your API key

Go to the cloud and setup your key, add your email address:

https://main.d3mpv0f3dqco4e.amplifyapp.com/register

```bash
ploomber cloud set-key $YOUR_API_KEY
```

```bash
ploomber cloud get-key
```

## Run your pipeline
We can get all of our pipeline execution history by running the command below, we can check out if we have anything that was errored out

```bash
ploomber cloud get-pipelines
```
now let's run the sample ml-basic pipeline and see how it's tracked

```python
%%sh --no-raise-error
ploomber build
```

Seeing how a successful pipeline looks like. You can also view the alerting mechanism - check out your email report!

```bash
ploomber cloud get-pipelines latest
```
![working-monitoring](https://ploomber.io/images/doc/monitoring-pipeline.png)

```python
from pathlib import Path

path = Path('fit.py')
clean = path.read_text()

# add a print statement at the end of 3-clean.py
path.write_text(clean + """
raise ValueError("This is a sample error in the model fit")
""")
```

```python
%%sh --no-raise-error
ploomber build
```

### Check your email
You should have a similar email stating a pipeline errored out and the error trace.

![errored-pip-monitoring](https://ploomber.io/images/doc/monitoring-pipeline.png)

You can also get all of the active pipelines, we'll see only ones that didn't finished yet.

```bash
ploomber cloud get-pipelines active
```

We can also delete errored pipelines if we'd like to for instance we can run the command below to delete the ml pipeline.


```python
%%sh --no-raise-error
ploomber cloud delete-pipeline 9448f7ee-cc90-4e8a-8539-98e2ed0b4061
```

# Conclusion
This short guide allows you to track your pipelines, it's especially relevant when running parallel/long executions and you want to be notified once your workflow has finished.

For more information you can check out the official guide: https://docs.ploomber.io/en/latest/cloud/index.html
