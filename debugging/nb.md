# Debugging

## Why debugging pipelines is hard

Debugging data pipelines is hard because there are three factors involved:

1. Our code
2. Input data
3. Parameters

In simple cases, the error message might give us enough information to fix the
bug, but in other cases (which happen more often), we'd want to inspect the
program while running to understand what's going on: see variable values,
run a few commands, etc).

Inspecting our program requires us to re-execute it under the same conditions
so we can replicate the conditions that led to the error.

depends on data - depends on the current inputs and derived inputs (from other tasks)

replicating a bug means running the same code with the same input data and parameters

## Debugger basics

A debugger is a program that help us inspect our program for debugging. Python
comes with its own debugger called
[`pdb`](https://docs.python.org/3/library/pdb.html)

There are a few approaches for debugging programs, one approach is line-by-line
debugging, which starts our program in *debug* mode so we can easily inspect
variables, move to the next line, etc.

One important concept to know when debugging are *stack frames*. Simply
speaking, stack frames represent the state of our code at a given level.
When a program fails, we might want to move between stack frames to know
how to fix a bug, as we will see in the next example.


## A tale of a buggy pipeline

Let's take a look at our example pipeline declaration:

```python
from ploomberutils import display_file
```

```python
display_file('pipeline.yaml')
```

Very simple, two tasks. One loads the data and the next one preprocess it. Let's run it (don't be scared by the long error message, scroll to the end where we will explain it):

```sh magic_args="--no-raise-error"
ploomber build --force
```

<!-- #region -->
If you followed the previous tutorial, you are already familiar with Ploomber's detailed error messages. Let's see the messages to understand what's going on.

The latest error message is the most general, the first one is the most specific. Let's take a look at the last one:

```
ploomber.exceptions.DAGBuildError: Failed to build DAG
```

Ok, this is very general. It's just saying the build process failed.

```
ploomber.exceptions.TaskBuildError: Error building task "preprocess"
```

That gives us more context. It's saying the specific task that failed.


```
ploomber.exceptions.TaskBuildError: An error ocurred when calling papermil.execute_notebook, partially executed notebook with traceback available at ...
```

That's useful, it's telling us where we can find the partially executed file in case we want to take a look at it.

```
ValueError: Found unknown categories ['d'] in column 1 during transform
```

Finally! The exact line that failed, if you take a look at the original message, you'll see that the actual line that raise the exception comes from the scikit-learn library.


This messages provide us with a lot of information: Our pipeline failed while trying to execute task `preprocess`. Somewhere in our task's code we ran something that made scikit-learn crash.

Let's take a look at the task's source code:
<!-- #endregion -->

```python
display_file('preprocess.py')
```

Our `preprocess.py` script is using scikit-learn's `OneHotEncoder` to transform variables. The error message offers some information but not enough to fix the issue, we don't have a column named "1"! So there must be something going on internally.

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
# COMMENT: After running "down" I see the line that raised the exception
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

This is an example of how your code could be doing everything right but your data is not compatible with it. How you fix this is up to. The important thing is to know why things are failing.
<!-- #endregion -->

<!-- #region -->
## Post-mortem debugging

Line-by-line debugging puts us at the beginning of the script and then we move as we want, an alternative approach is to let the program run and start the debugging session as soon as it finds an exception, this is called *post-mortem* debugging. The process is similar, we just have to change the kind of debugging we want:

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
# COMMENT: The session starts here. Not very useful because we inside the scikit-learn package
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

The previous example showed how we can debug a program that raises an exception. A more difficult scenario is when our program runs without errors but we find errors in the output (e.g. charts are not displaying correctly, data file has NAs, etc).

This is a much harder problem because we don't know where to look at! If a bug is originated in task `A` it might propagate to any downstream tasks that use the product from `A` as input. This is why testing is essential, by explicitly checking our data expectations, we increase the chance to track down the error at the source, rather than in any downstream task.

But when it happens (and trust me, it will). We recommend you to follow a recursive approach. Once you detect the error, the first question to answer is: Why task produced this output? Once you know that start a line-by-line debugging session (post-mortem won't work because there is no exception!), and carefully check variables to see if you can spot the error.

If everything looks correctly, go to the upstream tasks and repeat this process. You can do all of this from the command line.

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

## Using the CLI effectively

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
