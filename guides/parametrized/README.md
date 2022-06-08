<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n guides/parametrized`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fguides/parametrized%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=guides/parametrized%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/guides/parametrized/README.ipynb)
<!-- end header -->



# Parametrized pipelines

<!-- start description -->
Tutorial showing how to parametrize pipelines and change parameters from the command-line.
<!-- end description -->

Often, pipelines perform the same operation over different subsets of the data. For example, say you are developing visualizations of economic data. You might want to generate the same charts for other countries. 

One way to approach the problem is to have a for loop on each pipeline task to process all needed countries. But such an approach adds unnecessary complexity to our code; it's better to keep our logic simple (each task processes a single country) and take the iterative logic out of our pipeline.

Ploomber allows you to do so using parametrized pipelines. Let's see a sample using a `pipeline.yaml` file.

## Spec API (``pipeline.yaml``)


<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: print.py
    name: print
    product:
      nb: 'output/{{some_param}}/notebook.html'
    papermill_params:
        log_output: True
    params:
      some_param: '{{some_param}}'
```
<!-- #endmd -->

The `pipeline.yaml` above has a placeholder called `some_param`. It is coming from a file called `env.yaml`:

<!-- #md -->
```yaml
# Content of env.yaml
some_param: default_value
```
<!-- #endmd -->

When reading your `pipeline.yaml`, Ploomber looks for an `env.yaml` file. If found, all defined keys will be available to your pipeline definition. You can use these placeholders (placeholders are strings between double curly brackets) in any of the fields of your `pipeline.yaml` file.

In our case, we are using it in two places. First, we will save the executed notebook in a folder with the value of `some_param`; this will allow you to keep copies of the generated output in a different folder depending on your parameter. Second, if we want to use the parameter in our code, we have to pass it to our tasks; all tasks take an optional `params` with arbitrary parameters.

Let's see how the code looks like:

<!-- #md -->
```python
# Content of print.py
# + tags=["parameters"]
upstream = None
product = None
some_param = None

# +
print('some_param: ', some_param, ' type: ', type(some_param))

```
<!-- #endmd -->

Our task is a Python script, meaning that parameters are passed as an injected cell at runtime. Let's see what happens if we build our pipeline.

```python
%%capture captured
%%sh
ploomber build --force --log INFO
```

```python
def filter_output(captured, startswith):
    return print('\n'.join([
        line for line in captured.stderr.split('\n')
        if line.startswith(startswith)
    ]))

filter_output(captured, startswith='INFO:papermill:some_param')
```

We see that our param `some_param` is taking the default value (`default_value`) as defined in `env.yaml`. The command-line interface is aware of any parameters. You can see them using the `--help` option:

```sh
ploomber build --help
```

Apart from the default parameters from the `ploomber build` command, Ploomber automatically adds any parameters from `env.yaml`, we can easily override the default value. Let's do that:

```python
%%capture captured
%%sh
ploomber build --force --env--some_param another_value --log INFO
```

```python
filter_output(captured, startswith='INFO:papermill:some_param')
```

We see that our task effectively changed the value!

Finally, let's see how the `output/` folder looks like:

```sh
tree output
```

<!-- #region -->

We have separate folders for each parameter, helping to keep things organized and taking the looping logic out of our pipeline.


### Notes

* There are some built-in placeholders that you can use without having an `env.yaml` file. For example, `{{here}}` will expand to the `pipeline.yaml` parent directory. [Check out the Spec API documentation](https://docs.ploomber.io/en/latest/api/spec.html#default-placeholders) for more information.
* This example uses a Python script as a task. In SQL pipeline, you can achieve the same effect by using the placeholder in the product's schema or a table/view name prefix.
* If the parameter takes many different values and you want to run your pipeline using all of them, calling them by hand might get tedious. So you have two options 1) write a  bash script that calls the CLI with different value parameters or 2) Use the Python API (everything that the CLI can do, you can do with Python directly), take a look at the `DAGSpec` documentation.
* Parametrized `pipeline.yaml` files are a great way to simplify a task's logic but not overdo it. If you find yourself adding too many parameters, it's a better idea to use the Python AP directly; factory functions are the correct pattern for highly customized pipeline construction.
* Given that the two pipelines are entirely independent, we could even run them in parallel.


## Python API (factory functions)

Parametrization is straightforward when using a factory function. If your
factory takes parameters, they'll also be available in the command-line interface. Types are inferred from [type hints](https://docs.python.org/3/library/typing.html). Let's see an example:
<!-- #endregion -->

<!-- #md -->
```python
# Content of factory.py
from ploomber import DAG


def make(param: str, another: int = 10):
    dag = DAG()
    # add tasks to your pipeline...
    return dag

```
<!-- #endmd -->

Our function takes two parameters: `param` and `another`. Parameters with no default values (`param`) turn into positional arguments, and function parameters with default values convert
to optional parameters (`another`). To see the same auto-generated API, you can use the `--help` command:

```sh
ploomber build --entry-point factory.make --help
```

Note that the Python API requires more work than a `pipeline.yaml` file, but it is more flexible. [Click here] to see [examples](https://github.com/ploomber/projects/tree/master/python-api-examples) using the Python API.