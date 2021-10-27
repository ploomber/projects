<!-- start header -->
To run this example locally, [install Ploomber](https://ploomber.readthedocs.io/en/latest/get-started/install.html) and execute: `ploomber examples -n guides/debugging`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fguides/debugging%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=guides/debugging%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/guides/debugging/README.ipynb)
<!-- end header -->



<!-- #region -->
# Debugging

<!-- start description -->
Tutorial showing techniques for debugging pipelines.
<!-- end description -->

*For a quick reference,* [click here](https://ploomber.readthedocs.io/en/latest/cookbook/debugging.html).

## Why debugging pipelines is hard

Debugging data pipelines is hard because there are three factors involved:

1. Our code
2. Parameters
3. Input data

In simple cases, pipeline error messages might give us enough information to fix the
bug, but in other (which happen more often), we have to inspect the
program while running to understand what's going on: see variable values,
run a few diagnostic commands, etc.

Inspecting our program requires us to re-execute it under the same conditions
to replicate the crash. Replicating conditions means having the same code, parameters
and input data.

Getting the same code is easy if we know the version (i.e., git hash) running
during the crash. Replicating parameters involves more work; one way to approach
this is to ensure we always log parameters at the start of every pipeline execution.


Input data is more complex than it sounds. When our project is not properly assembled as a
data pipeline, we might run into issues if we use an incorrect file as input
(e.g. reading `/data/some-file.csv` instead of `/data/file.csv`). That's why Ploomber
puts a lot of emphasis on declaring products once and automatically propagating them
to any downstream consumers, to ensure that there is a single source of truth and we
always read if the appropriate file or SQL table from the upstream task.

As you can see, replicating error conditions accurately involves some work from your
end: 1) recording the project version and 2) input parameters (on every run) and 3) know
which input data led to the crash. Once you have these three pieces of information,
Ploomber will provide you tools to catch those sneaky bugs.


## Debugger basics

A debugger is a program that helps inspect another program for debugging. Python
comes with a debugger called
[pdb](https://docs.python.org/3/library/pdb.html).

There are a few approaches for debugging programs. One approach is line-by-line
debugging, which starts our program in *debug* mode so we can easily inspect
variables, move to the next line, etc.

One important concept to know when debugging is *stack frame*. Simply
speaking, stack frames represent the state of our code at a given level.
When you write a non-trivial function, it will depend on other
functions to work (yours or from third party packages). Each function has its
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
fail. If we pass `y=None`, the program fails, but it
will do so in the `reciprocal_and_multiply` function. For this trivial example,
it's easy to see at which level the code breaks but in a real program the source
code alone is usually not enough to know. Moving between stack frames can
help you find out where the error is coming from.
<!-- #endregion -->

## Tales of a buggy pipeline

Let's take a look at our example pipeline declaration:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: load.py
    product:
      nb: output/raw.ipynb
      train: output/train.csv
      test: output/test.csv

  - source: preprocess.py
    product: output/clean.ipynb

```
<!-- #endmd -->

Very simple, two tasks. One loads the data and the next one preprocess it.

Let's run it (don't be scared by the long error message, scroll until the end to see the explanation):

```sh magic_args="--no-raise-error"
ploomber build --force
```

<!-- #region -->
If you followed the previous tutorial, you are already familiar with Ploomber's structured error messages. So let's see the messages to understand what's going on.

The summary tells us the following

```
=============================== Summary (1 task) ===============================
NotebookRunner: preprocess -> File('output/clean.ipynb')
=============================== DAG build failed ===============================
```

The `preprocess` task failed. Go up a few lines:

```
ploomber.exceptions.TaskBuildError: An error occurred when calling papermil.execute_notebook, partially executed notebook with traceback available at ...
```

That's useful, it tells us where we can find the partially executed notebook in case we want to take a look at it. A few lines up:

```
ValueError: Found unknown categories ['d'] in column 1 during transform
```

That's the exact line that failed, if you take a look at the original error traceback, you'll see that the actual line that raised the exception comes from the scikit-learn library (`_encoders.py` file):

```
~/miniconda3/envs/ploomber/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py in _transform(self, X, handle_unknown)
    122                     msg = ("Found unknown categories {0} in column {1}"
    123                            " during transform".format(diff, i))
--> 124                     raise ValueError(msg)
    125                 else:
    126                     # Set the problematic rows to an acceptable value and

ValueError: Found unknown categories ['d'] in column 0 during transform
```


The error message provides us a lot of information: Our pipeline failed while executing task `preprocess`. Somewhere in our task's code we ran something that made scikit-learn crash.

Let's take a look at the failing task's source code:
<!-- #endregion -->

<!-- #md -->
```python
# Content of preprocess.py
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# + tags=["parameters"]
upstream = ['load']
product = None

# -


# +
def my_preprocessing_function(X_train, X_test):
    encoder = OneHotEncoder()
    X_train_t = encoder.fit_transform(X_train)
    X_test_t = encoder.transform(X_test)
    return X_train_t, X_test_t


# +
X_train = pd.read_csv(upstream['load']['train'])
X_test = pd.read_csv(upstream['load']['test'])

# +
my_preprocessing_function(X_train, X_test)

```
<!-- #endmd -->

Our `preprocess.py` script is using scikit-learn's `OneHotEncoder` to transform variables. The error message offers some information but not enough to fix the issue (*we don't have a column named "0"!*). There must be something going on internally.

This is a good use case for Ploomber's debugging capabilities.


## Starting line-by-line debugging sessions

To start a debugging session you first have to start an interactive session. To do so, run the following command in the terminal:

```console
ploomber interact
```

When it finishes setting things up, your pipeline will be available in the `dag` variable. This is a standard Python session, you can execute any Python code you want.

We already know that the error is happening in the `preprocess` task, you can start a line-by-line debugging session with the following command:

```pycon
>>> dag['preprocess'].debug()
```

Here's a replay of my debugging session (with comments):

```
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

Ah-ha! The encoder is fitted with a column with values `a`, `b` and `c` but then applied to a testing set with value `d`. That's why it's breaking.

This is an example of how your code could be doing everything right, but your data is incompatible. How you fix this is up to us. The important thing is that we know why things are failing.


## Post-mortem debugging

Line-by-line debugging puts us at the beginning of the script and then we move as we want. An alternative approach is to let the program run and start the debugging session as soon as it finds an exception, this is called *post-mortem* debugging. Starting a post-mortem session is similar: start and interactive session but then pass `kind='pm'` (`pm` stands for post-mortem) as argument to the `.debug()` function:

```pycon
>>> dag['preprocess'].debug(kind='pm')
```

Here's the (commented) replay of my post-mortem debugging session:

```
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

<!-- #region -->
## More difficult scenario: no exceptions raised but wrong output

The previous example showed how we could debug a program that raises an exception. A more difficult scenario is when our program runs without errors but we find issues in the output (e.g. charts are not displaying correctly, data file has NAs, etc).

This is a much harder problem because we don't know where to look at! If a bug is originated in task `A` it might propagate to any downstream tasks that use the product from `A` as input, this is why testing is essential. By explicitly checking our data expectations, we increase the chance of catching errors at the source, rather than in a downstream task.

When it happens (and trust me, it will), we recommend you to follow a recursive approach: Once you detect the error, the first question to answer is: Which task produced this output? Once you know that, start a line-by-line debugging session (post-mortem won't work because there is no exception!), and carefully check variables to see if you can spot the error.

If everything looks correct, go to all upstream tasks and repeat this process. You can do this from the command line.

First, start an interactive session from the terminal:

```console
ploomber interactive
```

Then debug the task that produced the buggy output:

```pycon
>>> dag['buggy_task'].debug()
```

If that's not enough, check upstream tasks. To find upstream tasks, use `task.upstream`:

```pycon
>>> dag['buggy_task'].upstream
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

## Using the CLI to check if we fixed the bug

In a real scenario, we might try a few things before we find bug fix. To quickly iterate over candidate solutions, we'd like to check if the applied change makes our pipeline *not* to throw an error. This is where Ploomber's incremental builds come in handy.

If we narrowed down the error to a specific task, we can apply changes and quickly check if the new code runs correctly by just running that task:

```console
ploomber task {task-name}
```

If the exception happens in task `B`, but the solution has to be implemented in task `A` (where `A` is an upstream dependency of `B`), then we have to make sure that we run `A` and `B` to verify the fix. A full end-to-end run is wasteful but so is an incremental run if `B` has many downstream tasks. For testing purposes, we just care about things going well *until `B`*. This is a good use of a partial build: it will run all tasks until it reaches a selected task (by default, it will still skip up-to-date tasks). In our case:

```console
ploomber build --partially B
```


## Letting our pipeline fail under unforeseen circumstances

The error in our program is of particular interest because it posits a common scenario: our program is correct but still failed due to unforeseen circumstances (unexpected data properties). Although these bugs challenge our assumptions about input data, fixing the error is just as important as explaining *why* we fixed the way we did it.

Picture this: we decide to drop all observations that contain the unexpected value (`d`), now our pipeline runs correctly. A few months later, we receive new data so we run the pipeline again, but we run into the same issue because of a new unexpected value (say, `e`).

We could argue that one solution would be to *drop all unexpected values*. Is this the best approach? Dropping observations silently is dangerous, as they might contain helpful information for our analysis. If we bury a `drop=True` piece of code in a pipeline with dozens of files, we will cause *a lot of* trouble to someone (which could be us) in the future. As we mentioned in the previous guide: explicitly stating our data expectations is the way to move forward.

If we decide dropping `d` is a reasonable choice, we can encode our new data expectations in the upstream task testing function (because that's the task that supplies input data). Let's recall how our pipeline looks like:
<!-- #endregion -->


<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: load.py
    product:
      nb: output/raw.ipynb
      train: output/train.csv
      test: output/test.csv

  - source: preprocess.py
    product: output/clean.ipynb

```
<!-- #endmd -->

`load` supplies input for `preprocess`. Our testing function for the `load` task would look like this:

<!-- #region -->
```python
def test_load(product):
    train = pd.read_csv(str(product['train']))
    test = pd.read_csv(str(product['test']))
    
    # NOTE: these are the expected values in the cat column
    # we expect value 'd' in the testing set and we'll
    # drop it during preprocessing. Any other unexpected
    # values will raise an exception here so we have the
    # chance to decide what to do with it
    assert set(train['cat'].unique()) == {'a', 'b', 'c'}
    assert set(test['cat'].unique()) == {'a', 'b', 'c', 'd'}
```

The comment should actually be part of the testing function, without it, there is no context to understand why are we testing such a specific condition.


## Debugging (templated) SQL scripts

So far, we've discussed how to debug Python scripts, but SQL scripts can also fail. In a previous guide, we showed how templated SQL scripts help us write more concise SQL code, but this comes with a cost. Relying too much on templating makes our templated source code short but hard to read. If your database complains about syntax errors when executing SQL tasks, chances are, the errors is coming from incorrect templating logic. One good first debugging step is to take a look at the rendered code. You can do so from the command line:

```console
ploomber task {task-name} --source
```

Apart from looking at rendered code, there isn't much to say about debugging SQL scripts because there are no interactive debuggers. The best we can do is to organize our scripts in a clear way to make it easy to spot errors.
<!-- #endregion -->

## Where to go next

* [pdb documentation](https://docs.python.org/3/library/pdb.html)