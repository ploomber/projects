# SQL/Python pipeline example

This demo showcases the spec API that allows you to write pipelines using YAML files so you can focus on the Data Science and not dealing which complex task dependencies nor managing database connections.

Let's take a look at the pipeline definition:

```sh
from pathlib import Path
from IPython.display import Markdown

Markdown('```yaml\n{}```'.format(Path('pipeline.yaml').read_text()))
```

The first two sections configure our pipeline, the `tasks` section is the actual pipeline definition. Each element defines a task, we see that we have a few SQL transformations, then we dump a table to a CSV file and we produce an HTML report at the end. The order here doesn't matter, the source code itself declares its own upstream dependencies and Ploomber extracts them to execute your pipeline.

Let's take a look at one of the SQL files:

```sh
Markdown('```yaml\n{}```'.format(Path('join.sql').read_text()))
```

Alright, let's get going, we can run our pipeline with the following command:

```sh
! ploomber build
```
That's it. We just build our pipeline. Let's try again.

```sh
! ploomber build
```

This time it finished real quick because there is nothing to do, nothing has changed.

Let's now modify one of the tasks to see what happens (make sure you save changes):

[Click here to open plot.py](plot.py)

Also try modifying any of the SQL scripts:

[Click here to go to the spec folder](.)

Let's build again:

```sh
! ploomber build
```

Depending on your changes, Ploomber will determine which tasks to run again and which ones to skip.

The final output of our pipeline is a report, [let's see it](output/plot.html).

That's it! Ploomber makes it very simple to manage your data workflows.


## Where to go from here

[`etl/`](../etl/README.ipynb) contains a more complete SQL example.
