<!-- #region -->
# Debugging

## Why debugging pipelines is hard

Debugging data pipelines is hard because there are three factors involved:

1. Our code
2. Parameters
3. Input data

In simple cases, pipeline error messages might give us enough information to fix the
bug, but in other (which happen more often), we have to inspect the
program while running to understand what's going on: see variable values,
run a few commands, etc).

Inspecting our program requires us to re-execute it under the same conditions
to replicate the crash. Replicating conditions means having the same code, parameters
and input data.

Getting the same code is easy if we know the version (or git hash) that was running
during the crash. Replicating parameters involves more work, one way to approach
this is to make sure we always log parameters at the start of every pipeline execution.


Input data is harder than it sounds, when our project is not properly assembled as a
data pipeline, we might run into issues if we are using the incorrect file as input
(e.g. reading `/data/some-file.csv` instead of `/data/file.csv`). That's why Ploomber
puts a lot of emphasis on declaring products one and automatically propagating them
to any downstream consumers, to ensure that we only declared a product once and we
always read if the appropriate file or SQL table.

As you can see, replicating error conditions accurately involve some work from your
end: recording the project version and input parameters on every run and making sure
you know which input data led to the crash. Once you have these three pieces of information,
Ploomber will provide you tools to catch those sneaky bugs.


## Debugger basics

A debugger is a program that helps inspect program for debugging. Python
comes with its own debugger called
[`pdb`](https://docs.python.org/3/library/pdb.html)

There are a few approaches for debugging programs. One approach is line-by-line
debugging, which starts our program in *debug* mode so we can easily inspect
variables, move to the next line, etc.

One important concept to know when debugging is *stack frame*. Simply
speaking, stack frames represent the state of our code at a given level.
When you write a non-trivial function, it will depend on other
functions (yours or from third party packages), each function has its
own stack frame which defines the variables that are available to it.

When a program fails, it can do so at different levels (i.e. a
different stack frame). Let's see a simple example:

```python
def reciprocal(x):
    return 1/x

def reciprocal_and_multiply(x, y):
    return reciprocal(x) * y
```

There are two places where things can go wrong in the program
above: if we pass `x=0`, the `reciprocal` operation will
fail. If we pass `y=None`, the program fails as well, but this time, it
will do so in the `reciprocal_and_multiply`. For this trivial example,
it's easy to see where things can fail but in a real program you won't
know, and moving between stack frames can help you find out where the
error is coming from.
<!-- #endregion -->

## Tales of a buggy pipeline

Let's take a look at our example pipeline declaration:

```python
from ploomberutils import display_file
```

```python
display_file('pipeline.yaml')
```

Very simple, two tasks. One loads the data and the next one preprocess it.

Let's run it (don't be scared by the long error message, scroll until the end to see the explanation):

```sh magic_args="--no-raise-error"
ploomber build --force
```

<!-- #region -->
If you followed the previous tutorial, you are already familiar with Ploomber's detailed error messages. Let's see the messages to understand what's going on.

The latest error message is the most general, the first one is the most specific. Let's take a look at the last one:

```pytb
ploomber.exceptions.DAGBuildError: Failed to build DAG
```

This is just saying the build process failed. Let's see the next one:

```pytb
ploomber.exceptions.TaskBuildError: Error building task "preprocess"
```

That gives us more context. It's saying the specific task that failed. Next one:


```pytb
ploomber.exceptions.TaskBuildError: An error ocurred when calling papermil.execute_notebook, partially executed notebook with traceback available at ...
```

That's useful, it's telling us where we can find the partially executed notebook in case we want to take a look at it. Finally:

```pytb
ValueError: Found unknown categories ['d'] in column 1 during transform
```

That's the exact line that failed, if you take a look at the original error traceback, you'll see that the actual line that raised the exception comes from the scikit-learn library (`_encoders.py` file):

```pytb
~/miniconda3/envs/ploomber/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py in _transform(self, X, handle_unknown)
    122                     msg = ("Found unknown categories {0} in column {1}"
    123                            " during transform".format(diff, i))
--> 124                     raise ValueError(msg)
    125                 else:
    126                     # Set the problematic rows to an acceptable value and

ValueError: Found unknown categories ['d'] in column 0 during transform
```


The error message provides us a lot of information: Our pipeline failed while trying to execute task `preprocess`. Somewhere in our task's code we ran something that made scikit-learn crash.

Let's take a look at the failing task's source code:
<!-- #endregion -->

```python
display_file('preprocess.py')
```

Our `preprocess.py` script is using scikit-learn's `OneHotEncoder` to transform variables. The error message offers some information but not enough to fix the issue (*we don't have a column named "0"!*). There must be something going on internally.

This is a good use case for Ploomber's debugging capabilities.

<!-- #region -->
## Starting line-by-line debugging sessions

To start a debugging session you first have to start an interactive session. To do so, run the following command in the terminal:

```sh
ploomber interact
```

When it finishes setting things up, your pipeline will be available in the `dag` variable. This is a standard Python session, you can execute any Python code you want.

We already know that the error is happening in the `preprocess` task, you can start a line-by-line debugging session with the following command:

```python
dag['preprocess'].debug()
```

Here's a replay of my debugging session (with comments):

```python
# COMMENT: I entered the command "next" a few times until I reached the failing line
ipdb>
> /var/folders/3h/_lvh_w_x5g30rrjzb_xnn2j80000gq/T/tmpbatitar6.py(45)<module>()
     41 X_train = pd.read_csv(upstream['load']['train'])
     42 X_test = pd.read_csv(upstream['load']['test'])
     43
     44 # + tags=[]
# COMMENT: "--->" means that line will be executed when I send the "next" command
---> 45 my_preprocessing_function(X_train, X_test)

ipdb>
# COMMENT: Same error message that we got before!
ValueError: Found unknown categories ['d'] in column 0 during transform
> /var/folders/3h/_lvh_w_x5g30rrjzb_xnn2j80000gq/T/tmpbatitar6.py(45)<module>()
     41 X_train = pd.read_csv(upstream['load']['train'])
     42 X_test = pd.read_csv(upstream['load']['test'])
     43
     44 # + tags=[]
---> 45 my_preprocessing_function(X_train, X_test)
# COMMENT: I entered the "down" command to move one stack frame down (inside my_preprocessing_function)
ipdb> down
> /var/folders/3h/_lvh_w_x5g30rrjzb_xnn2j80000gq/T/tmpbatitar6.py(36)my_preprocessing_function()
     34     encoder = OneHotEncoder()
     35     X_train_t = encoder.fit_transform(X_train)
# COMMENT: The line that raised the exception
---> 36     X_test_t = encoder.transform(X_test)
     37     return X_train_t, X_test_t
     38

# COMMENT: Print X_train and X_test
ipdb> X_train
  cat
0   a
1   b
2   c
ipdb> X_test
  cat
0   a
1   b
2   d
# COMMENT: Exit debugger with the "quit" command
ipdb> quit
```

Ah-ha! The encoder is fitted with a column that has values `a`, `b` and `c` but then is applied to a testing set that has value `d`. That's why it's breaking.

This is an example of how your code could be doing everything right but your data is not compatible with it. How you fix this is up to. The important thing is that we know why things are failing.
<!-- #endregion -->

<!-- #region -->
## Post-mortem debugging

Line-by-line debugging puts us at the beginning of the script and then we move as we want. An alternative approach is to let the program run and start the debugging session as soon as it finds an exception, this is called *post-mortem* debugging. Starting a post-mortem session is similar: start and interactive session but then pass `kind='pm'` as argument to the `.debug()` function:

```python
# pm stands for post-mortem
dag['preprocess'].debug(kind='pm')
```

Here's the (commented) replay of my post-mortem debugging session:

```python
# COMMENT: I deleted a few lines for brevity
ValueError: Found unknown categories ['d'] in column 0 during transform
> /Users/Edu/miniconda3/envs/ploomber/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py(124)_transform()
    122                     msg = ("Found unknown categories {0} in column {1}"
    123                            " during transform".format(diff, i))
# COMMENT: The session starts here. Not very useful because we are inside the scikit-learn package
# (note the file path: site-packages/sklearn/preprocessing/_encoders.py)
--> 124                     raise ValueError(msg)
    125                 else:
    126                     # Set the problematic rows to an acceptable value and
# COMMENT: Let's move up
ipdb> up
> /Users/Edu/miniconda3/envs/ploomber/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py(428)transform()
    426         check_is_fitted(self)
    427         # validation of X happens in _check_X called by _transform
--> 428         X_int, X_mask = self._transform(X, handle_unknown=self.handle_unknown)
    429
    430         n_samples, n_features = X_int.shape
# COMMENT: Still inside scikit-learn, let's move up again
ipdb> up
> /var/folders/3h/_lvh_w_x5g30rrjzb_xnn2j80000gq/T/tmp653y199s.py(36)my_preprocessing_function()
     34     encoder = OneHotEncoder()
     35     X_train_t = encoder.fit_transform(X_train)
# COMMENT: Now are are in our task's code, same place as in the previous example
---> 36     X_test_t = encoder.transform(X_test)
     37     return X_train_t, X_test_t
     38
ipdb> X_train
  cat
0   a
1   b
2   c
ipdb> X_test
  cat
0   a
1   b
2   d
ipdb> quit
```

As you can see, we can use either of these two approaches.
<!-- #endregion -->

<!-- #region -->
## More difficult scenario: Wrong output but no exceptions raised

The previous example showed how we can debug a program that raises an exception. A more difficult scenario is when our program runs without errors but we find issues with the output (e.g. charts are not displaying correctly, data file has NAs, etc).

This is a much harder problem because we don't know where to look at! If a bug is originated in task `A` it might propagate to any downstream tasks that use the product from `A` as input, this is why testing is essential. By explicitly checking our data expectations, we increase the chance of catching errors at the source, rather than in a downstream task.

When it happens (and trust me, it will), we recommend you to follow a recursive approach: Once you detect the error, the first question to answer is: Which task produced this output? Once you know that start a line-by-line debugging session (post-mortem won't work because there is no exception!), and carefully check variables to see if you can spot the error.

If everything looks correct, go to all upstream tasks and repeat this process. You can do this from the command line.

First, start an interactive session from the terminal:

```sh
ploomber interactive
```

Then debug the task that produced the buggy output:

```python
dag['buggy_task'].debug()
```

If that's not enough, check upstream tasks. To find upstream tasks, use `task.upstream`:

```python
dag['buggy_task'].upstream
```

If you have a hypothesis of *where the error might be*. You can insert a breakpoint in your task's source code to start a debugging session at any given point:


```python
# buggy_task.py

# some code
# ...
# ...

# breakpoint: this is where I think the bug is...
import pdb; pdb.set_trace()


# more code
# ...
# ...
```

Then start a post-mortem session. The debugger will start at the line where you inserted the breakpoint.

## Defensive programming

add assertions

## Using the CLI to check if we fixed the bug

ploomber task -f, ploomber build --partially task


## Debugging (templated) SQL scripts

Ploomber uses templated SQL to assemble the pipeline and to provide a way to write more concise SQL scripts, but this comes with a cost. Relying too much on templating makes our raw source code concise but hard to read. If you run into syntax error issues when executing your SQL queries, the first things to do is to see the rendered code, you can do so from the command line:

```
ploomber task {task-name} --source
```
<!-- #endregion -->


## Where to go next

* [`pdb` documentation](https://docs.python.org/3/library/pdb.html)

```python

```
