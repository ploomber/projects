# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Micro-pipelines inside Jupyter notebooks
#
# *Added in version 0.20.1*
#
# Jupyter notebooks can get very [messy](https://ploomber.io/blog/clean-nbs/) due to many reasons: cells are executed out of order, data frames are modified, no modularity. Ploomber micro-pipelines are a more powerful version of [`sklearn.pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
#
# You can use Ploomber as a framework to write micro-pipelines that capture your data transformation logic enabling you to:
#
# - Write cleaner code
# - Re-use components
# - Easily parallelize transformations
# - Cache results
#
# Let's see how this works:

# %% [markdown]
# ## Transformations as functions

# %%
import pandas as pd

# the "root" transformations (tasks with no dependencies)
# need an input_data argument
def ones(input_data):
    return pd.Series(input_data)


# to use previous results, add names of
# other functions as arguments. For example,
# here, we'll use the output of "ones" as input
def twos(ones):
    return ones + 1


def both(ones, twos):
    return pd.DataFrame({"ones": ones, "twos": twos})


def final(both):
    both["final"] = both["ones"] + both["twos"] + 1
    return both

def one_more(ones):
    return ones + 1


# %% [markdown]
# ## Creating the pipeline
#
# To create the dag, pass the list of functions. Ploomber will automatically figure out the dependencies and execution order.
#
# In the `params` argument, pass the input data for tasks that have no dependencies.

# %%
from ploomber.micro import dag_from_functions, grid, capture
from ploomber import InMemoryDAG

dag = dag_from_functions(
        [ones, twos, both, final, one_more],
        params={"ones": {"input_data": [1] * 100}},
        # store intermediate results in the cache/ directory
        output="cache"
    )

# %% [markdown]
# Note that `dag` is a regular Ploomber DAG so we have all the features:
#
# - Incremental builds
# - Debug later
# - Parallelization, etc.
#
# *Note:* To run tasks in parallel, pass `parallel=True`; however, parallel execution is in beta. If you encounter issues. [Let us know.](https://github.com/ploomber/ploomber/issues/new?title=problem%20with%20micro%20pipelines%20api)
#
# ## Plotting the pipeline

# %%
dag.plot()

# %% [markdown]
# ## Executing the pipeline

# %%
dag.build()

# %% [markdown]
# ## Caching results

# %% [markdown]
# If we execute again, nothing will run since we have cached the results:

# %%
dag.build()

# %% [markdown]
# Now, modify one of the functions in the pipeline (and re-execute the cell, then come back and execute `.build()` again, you'll see that only affected tasks are executed:

# %%
dag.build()

# %% [markdown]
# ## Loading outputs
#
# Let's load the output of some task

# %%
dag["ones"].load().head(3)

# %% [markdown]
# ## In memory pipeline
#
# `dag` serializes outputs for caching, this is useful for development. However, for production, you might want to convert into a full in-memory pipeline:

# %%
in_memory = InMemoryDAG(dag)

# %% [markdown]
# To run it, pass a dictionary with the input data for tasks with no dependencies to `input_data`:

# %%
out = in_memory.build(input_data={"ones": [1] * 10})

# %% [markdown]
# `out` is a dictionary, where keys are task names and values are the outputs:

# %%
out["ones"].head(3)

# %%
out["final"].head(3)

# %% [markdown]
# Let's try with a different input value:

# %%
in_memory.build(input_data={"ones": [1.1] * 10})["final"].head(3)


# %% [markdown]
# ## Grid tasks (parametrization)
#
# In some cases (for example, when training ML models), you might want to run the same function with grid of parameters, you can do so with the `@grid` decorator:

# %%
@grid(value=[0, 1, 2])
def add(ones, value):
    return ones + value

dag_grid = dag_from_functions(
    [ones, add],
    params={"ones": {"input_data": [1] * 100}},
    output="cache-grid",
    parallel=True,
)

dag_grid.plot()

# %% [markdown]
# You can check the parameter of each task:

# %%
print(dag_grid['add-0'].params['value'])
print(dag_grid['add-1'].params['value'])
print(dag_grid['add-2'].params['value'])

# %%
dag_grid.build()


# %% [markdown]
# You can use more than one parameter in the `@grid`, the number of tasks will be the cartesian product:

# %%
# generates: 3 * 3 = 9 tasks
@grid(value=[0, 1, 2], another=[3, 4, 5])
def add_two_params(ones, value, another):
    return ones + value + another

dag_grid_two = dag_from_functions(
    [ones, add_two_params],
    params={"ones": {"input_data": [1] * 100}},
    output="cache-grid",
    parallel=True,
)

dag_grid_two.plot()


# %% [markdown]
# You can also use the decorator more than once:

# %%
# generates:
# (3 * 3) + (3 * 3) = 18 tasks
@grid(value=[0, 1, 2], another=[3, 4, 5])
@grid(value=[6, 7, 8], another=[8, 10, 11])
def add_double(ones, value, another):
    return ones + value + another

dag_double = dag_from_functions(
    [ones, add_double],
    params={"ones": {"input_data": [1] * 100}},
    output="cache-grid",
    parallel=True,
)

dag_double.plot()


# %% [markdown]
# ## Debugging
#
# To debug a pipeline, you can use the `debug` argument when calling `dag.build()`:

# %%
def crashing(ones, twos):
    x, y = 1, 0
    return x / y


dag_debug = dag_from_functions(
    [ones, twos, crashing],
    params={"ones": {"input_data": [1] * 100}},
    output="cache-debugging",
    parallel=True,
)

# %%
dag_debug.plot()


# %% [markdown]
# Start a debugging session as soon as the pipeline crashes:
#
# ```python
# dag_debug.build(debug='now')
# ```
#
# Serialize all tracebacks for later debugging:
#
# ```python
# dag_debug.build(debug='later')
# ```
#
# For more details, see the [debugging guide.](https://docs.ploomber.io/en/latest/user-guide/debugging.html)

# %% [markdown]
# ## Re-using components
#
# Your functions are re-usable, let's create a new pipeline by re-using two components and adding one more:

# %%
def multiply(ones, twos):
    df = pd.DataFrame({"mult": ones * twos})
    return df


dag_another = dag_from_functions(
    [ones, twos, multiply],
    output="cache-2",
    params={"ones": {"input_data": [1] * 100}},
    parallel=True,
)

# %%
dag_another.plot()

# %%
dag_another.build()

# %%
dag_another["multiply"].load().head(3)


# %% [markdown]
# ## Writing generic components
#
# Note that in the previous example, our `multiply` function had `ones` and `twos` as arguments. But what if we wanted to have a generic function like:

# %%
def multiply(first, second):
    return first * second


# %% [markdown]
# In this case, we can use the `dependencies` argument, to set the dependencies when the arguments do not match existing functions:

# %%
dag_generic = dag_from_functions(
    [ones, twos, multiply],
    output="cache-generic",
    params={"ones": {"input_data": [1] * 100}},
    # order matters:
    # output of "ones" -> "first"
    # output of "twos" -> "second"
    dependencies={"multiply": ["ones", "twos"]},
    parallel=True,
)

# %%
dag_generic.plot()

# %%
dag_generic.build(force=True)

# %%
dag_generic["ones"].load().head(3)

# %%
dag_generic["twos"].load().head(3)

# %%
dag_generic["multiply"].load().head(3)
