<!-- #region -->
# Pipeline testing

Testing your pipeline is critical to ensure your data expectations hold. When you perform a transformation in a dataset, you are expecting the output to have certain properties (e.g. no nulls in certain column).

Not testing your expectations is risky, since errors will propagate to all downstream tasks.

Here's a list of common sources of errors:

1. A join operation generates duplicated entries because a wrong assumption of a one-to-one relationship (which is really a one-to-many)
2. A function that aggregates data returns `NULL` because at least one of the data points was `NULL`
4. Dirty data points are used in the analysis (e.g. in a column `age`, you forgot to remove corrupted data points with negative values)

To make testing effective, **your tests should run every time you run your tasks**. Fortunately, this is easy to do with Ploomber.


TODO: mention that tests check your code but also the data. your code might be working now but if the data changes, your code might not work anymore (e.g. column rename) - critical to run tests every time instead of just when your code changes!

This example loads data from a single table called `my_table`, which has two columns:

1. age: ranges from 21 to 80 but there are some corrupted records with -42
2. score: ranges from 0 to 10 but there are some corrupted records with missing values

Let's take a look at our example `pipeline.yaml`:
<!-- #endregion -->

```python
from pathlib import Path
from ploomberutils import display_file
```

```python
display_file('pipeline.yaml')
```

<!-- #region -->
The pipeline has three tasks, one to clean the raw table, another one to dump the clean data to a csv file and finally, one Python task to transform the data. We included a SQL and a Python task to show how you can test both types of tasks.

The configuration is straightforward, the only new key is `on_finish`. This is known as a "task hook". Task hooks allow you to embed custom logic when certain events happen. `on_finish` is executed after a task succesfully finishes. The value is a dotted path, which tells Ploomber where to find your testing function. Under the hood, Ploomber dynamically import your function and calls it after the task is executed, here's some equivalent code:

```python
from integration_tests import test_sql_clean

# your task is executed...

# ploomber calls your testing function...
test_sql_clean()
```

Before diving into the testing source code, let's see the rest of the tasks.

`clean.sql` just filters columns we don't want to include in the analysis:
<!-- #endregion -->

```python
display_file('clean.sql')
```

`dump.sql` just selects all rows from the clean table to dump it to the CSV file:

```python
display_file('dump.sql')
```

Finally, the `transform.py` script generates a new column using `some_value`

```python
display_file('transform.py')
```

Let's now take a look at our tests:

```python
display_file('integration_tests.py')
```

<!-- #region -->
## Testing Python scripts

To test your Python scripts, you have to know which file to look at. You can do so by simply adding `product` as argument to your function. `product` will be a dictionary-like object. If your Python script generates more than one product (like in our case), you have to pass the key to the object. To get the path to the product, simply use the `str` function.

```python
# dictionary-like object: maps names to product objects
product

# product object
product['data']

# path to the data file
str(product['data'])
```

## Testing SQL scripts

To test SQL scripts, you also need the client to send queries to the appropriate database, to do so, just add `client` to your testing function.

The `ploomber.testing.sql` module implements convenient functions to test your tables. They always take client as the first argument. You just have to pass the client object directly.

Since our SQL script only generates a product, you can directly pass the product obejct to the testing function. Otherwise, you'd have to use `product[key]`. If you're implementing your own SQL testing logic, doing `str(product)` will return a `{schema}.{name}` string, you can also use `product.schema` and `product.name`.

## Running the pipeline

We now run the pipeline:
<!-- #endregion -->

```sh
ploomber build
```

Everything looks good. Let's now imagine a colleague found an error in the cleaning logic and has re-written the script. However, she was unaware that both columns in the raw table had corrupted data and forgot to include the filtering conditions. The script now looks like this:

```python
path = Path('clean.sql')
new_code = path.read_text().replace('WHERE some_value is not null AND age > 0', '')
path.write_text(new_code)
display_file('clean.sql')
```

Let's see what happens if we run the pipeline (don't be intimidated by the long traceback, we'll explain it in a bit):

```python
%%capture captured
%%sh --no-raise-error
ploomber build
```

```python
print(captured.stderr)
```

Ploomber error messages are designed to give you as much context as they can, so you can fix things quickly. The last line says that our pipeline failed to build:

```
ploomber.exceptions.DAGBuildError: Failed to build DAG
```

That's a very general error message, if you go up a few lines, you'll see this:

```
ploomber.exceptions.TaskBuildError: Exception when running on_finish for task "clean"
```

That's a bit more specific. It's telling me I have to look at the `on_finish` hook in the `clean` task. Go up a few more lines:

```
assert not nulls_in_columns(client, ['some_value', 'age'], product)
AssertionError
```

That tells me the exact test that failed! While having this long error messages might seem to verbose, it helps a lot to understand why the pipeline failed: "the pipeline building process failed because the `on_finish` hook in task `clean` raised an exception in this line". That's much better than either "the pipeline failed" or "this line raised an exception".

Let's fix our pipeline and add the `WHERE` clause again:

```python
path = Path('clean.sql')
new_code = path.read_text() + 'WHERE some_value is not null AND age > 0'
path.write_text(new_code)
display_file('clean.sql')
```

```sh
ploomber build
```

<!-- #region -->
All good! Pipeline is running without issues.

## Test-driven development (TDD)

Writing data tests is essential for developing robust pipelines. Coding tests is simple, all we have to do is write in code that we already have in our mind when thinking what we want the outcome of a given script to be.

This thought process happens *before* we write the actual data transformation code, which means we could easily write tests first and then code our transformation logic. This approach is called Test-driven development (TDD).

Following this framework has an added benefit, since we force ourselves to put in concrete terms (the tests) our data expectations, it will be easier to then think how we want to get there. In this way, *tests also serve as documentation* for us (and for others). By looking at our tests, anyone can see what *our intent* is, then by looking at the actual code, it will be easier to spot errors between our intent and our implementation.


## Pro tip: debugging and developing tests interactively

Even though tests are usually just a few short statements, writing them in an interactive way is more productive. One simple trick you can use to do this is to start an interactive session with the appropriate execution context, that is, with the `client` and `product` variables available for you to write the tests.

Let's imagine you want to write a test for a new SQL script (but the same applies for other scripts), so you add a new function:

```python
def my_sql_testing_function(client, product):
    pass
```

To start an interactive session, just add the following line:

```python
def my_sql_testing_function(client, product):
    from IPython import embed; embed()
```

Next time you call `ploomber build`, an interactive Python session will start right when your function is about to execute, you can verify that by running:

```
print(client)
print(product)
```


## Where to go next

* [Our blog post on CI for Data Science (which includes a section on testing pipelines)](https://towardsdatascience.com/rethinking-continuous-integration-for-data-science-ebf0dfc61788)
<!-- #endregion -->
