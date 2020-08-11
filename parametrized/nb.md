# Parametrized pipelines

Often, pipelines perform the same operation over different subsets of the data. For example, say you are developing visualizations of economic data. You might want to generate the same charts for different countries. 

One way to approach the problem is to have a for loop on each pipeline task to process all countries you need. But such approach adds unnecessary complexity to our code, it's better to keep our logic simple (each task processes a single country) and take the iterative logic out of our pipeline.

Ploomber allows you to do so using parametrized pipelines. Let's see a sample `pipeline.yaml`:

```python
from pathlib import Path
from IPython.display import Markdown, display
```

```python
def print_file(path):
    path = Path(path)
    kind = path.suffix.replace('.', '')
    content = path.read_text()
    display(Markdown("""
```{}
{}
```
""".format(kind, content)))
    
def print_papermill_output(captured):
    return print('\n'.join([l for l in captured.stderr.split('\n') if l.startswith('INFO:papermill:some_param')]))
```

```python
print_file('pipeline.yaml')
```

The `pipeline.yaml` above has a placeholder called `some_param`. It is coming from a file called `env.yaml`:

```python
print_file('env.yaml')
```

When assembling your pipeline, Ploomber looks for an `env.yaml` file. If found, all defined keys will be available to your pipeline definition. You can use these placeholders (placeholders are strings between double curly brackets) in any of the fields of your `pipeline.yaml` file.

In our case, we are using it in two places. First, we are going to save the executed notebook in a folder with the value of `some_param`. This will allow you to keep copies of the generated output in a different folder depending on your parameter. Second, if we want to use the parameter in our code, we have to pass it to our tasks, all tasks take an optional `params` with arbitrary parameters.

Let's see how the code looks like:

```python
print_file('print.py')
```

Our task is a Python script. This means parameters are passed as an injected cell at runtime. Let's see what happens if we build our pipeline.

```python
%%capture captured
%%sh
ploomber build --force --log INFO
```

```python
print_papermill_output(captured)
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
print_papermill_output(captured)
```

We see that our task, effectively changed the value!

Finally, let's see how the `output/` folder looks like:

```sh
tree output
```

We have separate folders for each parameter, this helps keep things organized and takes the looping logic out of our pipeline. Parametrized pipelines are a great way to simplify our task's logic. Given that the two pipelines are completely independent we could even think of running them in parallel to speed things up.
