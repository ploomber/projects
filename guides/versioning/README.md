<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n guides/versioning`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/guides/versioning/README.ipynb)
<!-- end header -->



# Versioning

**Note:** This feature requires Ploomber 0.17.1 or higher.

<!-- start description -->
A tutorial showing how to version pipeline products.
<!-- end description -->

Although Ploomber is not a data versioning solution, it offers a simple way to organize pipeline artifacts via placeholders. Note that this requires your project to be in a git repository.


## Using `{{git}}`

Let's look at the first example, which uses the `{{git}}` placeholder:

<!-- #md -->
```yaml
# Content of pipeline.git.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: 'output/{{git}}/load.html'
      data: 'output/{{git}}/data.csv'

  - source: tasks/plot.py
    product:
      nb: 'output/{{git}}/plot.html'
```
<!-- #endmd -->

You can see that both tasks use `{{git}}`. When Ploomber executes the pipeline, it will replace the placeholder using the following order:

1. If currently at the tip of the branch, return the branch name
2. If the current commit has a tag, return the tag name
3. Otherwise, return the hash for the current commit (appending `-dirty` if there are [uncommitted changes](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gitglossary.html#def_dirty))

Let's see how it works:

```python
from pathlib import Path

from ploomber.spec import DAGSpec
```

```python
dag = DAGSpec('pipeline.git.yaml').to_dag()
dag['load'].product['nb']
```

We can see the product will be stored in the `output/master` directory, `{{git}}` is resolved to `master` since we're at the tip of such branch.


## Using `{{git_hash}}`

The `{{git_hash}}` placeholder is similar to `{{git}}`, except it doesn't return the branch name, the rules are as follows:

1. If the current commit has a tag, return the tag name
2. Otherwise, return the hash for the current commit (appending `-dirty` if there are [uncommitted changes](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gitglossary.html#def_dirty))

This is how our sample `pipeline.git_hash.yaml` looks like:

<!-- #md -->
```yaml
# Content of pipeline.git_hash.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: 'output/{{git_hash}}/load.html'
      data: 'output/{{git_hash}}/data.csv'

  - source: tasks/plot.py
    product:
      nb: 'output/{{git_hash}}/plot.html'
```
<!-- #endmd -->

```python
dag = DAGSpec('pipeline.git_hash.yaml').to_dag()
dag['load'].product['nb']
```

This time, the product will be stored in a directory with the hash of the current commit.


## Adding the current timestamp with `{{now}}`

Alternatively, you can use the `{{now}}` placeholder, which doesn't require your project to be in a git repository and will resolve to the current timestamp:

<!-- #md -->
```yaml
# Content of pipeline.now.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: 'output/{{now}}/load.html'
      data: 'output/{{now}}/data.csv'

  - source: tasks/plot.py
    product:
      nb: 'output/{{now}}/plot.html'
```
<!-- #endmd -->

```python
dag = DAGSpec('pipeline.now.yaml').to_dag()

path = Path(dag['load'].product['nb']).relative_to(Path().resolve())
print(path)
```

You can see that the `load.html` file will to into a folder with the timestamp computed when running this example.


## Using placeholders in selected tasks

You can selectively choose which tasks to organize based on the git repository commit, the following example only uses the `{{git}}` placeholder in the last task:

<!-- #md -->
```yaml
# Content of pipeline.partial.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: 'output/load.html'
      data: 'output/data.csv'

  - source: tasks/plot.py
    product:
      nb: 'output/{{git}}/plot.html'
```
<!-- #endmd -->

```python
dag = DAGSpec('pipeline.partial.yaml').to_dag()
dag['load'].product['nb']
```

```python
dag['plot'].product['nb']
```

Here, you can see that the product of the `load` task goes to `output/`, while the output of `plot` goes to `output/master/`


## Using an `env.yaml`

If you're using an `env.yaml` file, you can still use the placeholders:

```yaml
# env.yaml
directory: '{{git}}' # or '{{git_hash}}'
```

Then add references to `{{directory}}` in your `pipeline.yaml`:

```yaml
# pipeline.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: 'output/{{directory}}/load.html'
      data: 'output/{{directory}}/data.csv'
```
