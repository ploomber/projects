# Parametrized pipelines

**Note:** This page was generated form a Jupyter notebook. [Click here](https://github.com/ploomber/projects/tree/master/parametrized/nb.md) to see the source code. [Or here](https://mybinder.org/v2/gh/ploomber/projects/master?filepath=parametrized%2Fnb.md) to launch an interactive demo.


Often, pipelines perform the same operation over different subsets of the data. For example, say you are developing visualizations of economic data. You might want to generate the same charts for different countries. 

One way to approach the problem is to have a for loop on each pipeline task to process all countries you need. But such approach adds unnecessary complexity to our code, it's better to keep our logic simple (each task processes a single country) and take the iterative logic out of our pipeline.

Ploomber allows you to do so using parametrized pipelines. Let's see a sample `pipeline.yaml`.


## Spec (``pipeline.yaml``)

```python
from ploomberutils import display_file, filter_output
```

```python
display_file('pipeline.yaml')
```

The `pipeline.yaml` above has a placeholder called `some_param`. It is coming from a file called `env.yaml`:

```python
display_file('env.yaml')
```

When assembling your pipeline, Ploomber looks for an `env.yaml` file. If found, all defined keys will be available to your pipeline definition. You can use these placeholders (placeholders are strings between double curly brackets) in any of the fields of your `pipeline.yaml` file.

In our case, we are using it in two places. First, we are going to save the executed notebook in a folder with the value of `some_param`. This will allow you to keep copies of the generated output in a different folder depending on your parameter. Second, if we want to use the parameter in our code, we have to pass it to our tasks, all tasks take an optional `params` with arbitrary parameters.

Let's see how the code looks like:

```python
display_file('print.py')
```

Our task is a Python script. This means parameters are passed as an injected cell at runtime. Let's see what happens if we build our pipeline.

```python
%%capture captured
%%sh
ploomber build --force --log INFO
```

```python
filter_output(captured, startswith='INFO:papermill:some_param')
```

We see that our param `some_param` is taking the default value (`default_value`) as defined in `env.yaml`. The command line interface is aware of any parameters, you can see them using the `--help` option:

```sh
ploomber build --help
```

Apart from the default parameters from the `ploomber build` command, Ploomber automatically adds any parameters from `env.yaml`, we can easily override the default value, let's do that:

```python
%%capture captured
%%sh
ploomber build --force --env__some_param another_value --log INFO
```

```python
filter_output(captured, startswith='INFO:papermill:some_param')
```

We see that our task, effectively changed the value!

Finally, let's see how the `output/` folder looks like:

```sh
tree output
```

<!-- #region -->
We have separate folders for each parameter, this helps keep things organized and takes the looping logic out of our pipeline.


### Tips

* This example uses a Python script as a task, in SQL pipeline, you can achieve the same effect (keeping output separate) by using the placeholder either in the product's schema or as a prefix in the table/view name
* If the parameter takes a lot of different values and you want to run your pipeline using all of them, calling them by hand might get tedious. You have two options 1) write a  bash script that calls the CLI with different value parameters or 2) Use the Python API (everything that the CLI can do, you can do with Python directly), take a look at the `DAGSpec` documentation
* Parametrized `pipeline.yaml` files are a great way to simplify task's logic but don't overdo it. If you find yourself adding too many parameters, it's a better idea to use the Python API directly. Factory function are the right pattern for highly customized pipeline construction
* Given that the two pipelines are completely independent we could even run them in parallel to speed things up


## Factory functions

Parametrization is straightforward when using a factory function. If your
factory takes parameters, they'll also be available in the command
line interface. Types are inferred from [type hints](https://docs.python.org/3/library/typing.html). Let's see an example:
<!-- #endregion -->

```python
display_file('factory.py')
```

Our function takes two parameters: `param` and `another`. Parameters with no default values (`param`) are converted to positional arguments and function parameters with default values are converted
to optional parameters (`another`). To see the exact auto-generated API, you can use the `--help` command:

```sh
ploomber build --entry-point factory.make --help
```
