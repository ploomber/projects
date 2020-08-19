# Pipeline testing

Testing your pipeline is critical to ensure your data expectations hold. When you perform a data transformation, you are expecting the output to have certain properties (e.g. no nulls in certain column). Without testing, these expectations won't be verified and will cause errors errors to propagate to all downstream tasks.

These are the most common sources of errors when transforming data:

1. A join operation generates duplicated entries because a wrong assumption of a one-to-one relationship (which is really a one-to-many) in the source tables
2. A function that aggregates data returns `NULL` because at least one of the input data points was `NULL`
3. Dirty data points are used in the analysis (e.g. in a column `age`, you forgot to remove corrupted data points with negative values)

Some of these errors are easy to spot (2), but it might take you some tome to find out about others (1 and 3), or worst, you will never notice these errors and just use incorrect data in your analysis. And even if your code is correct and all your expectations hold true, it might not hold true in the future if the data changes and it's important for you to know this as soon as it happens.

To make testing effective, **your tests should run every time you run your tasks**. Ploomber has a mechanism to automate this.

## Sample data

This example loads data from a single table called `my_table`, which has two columns:

1. age: ranges from 21 to 80 but there are some corrupted records with -42
2. score: ranges from 0 to 10 but there are some corrupted records with missing values

Let's take a look at our example `pipeline.yaml`:

```python
from pathlib import Path
from ploomberutils import display_file
```

```python
display_file('pipeline.yaml')
```

<!-- #region -->
The pipeline has three tasks, one to clean the raw table, another one to dump the clean data to a CSV file and finally, one Python task to transform the data. We included a SQL and a Python task to show how you can test both types of tasks but we recommend you to do as much analysis as you can using SQL because it scales much better than Python code (you won't have to deal with memory errors).

The configuration is straightforward, the only new key is `on_finish` (inside the first and third task). This is known as a *hook*. Task hooks allow you to embed custom logic when certain events happen. `on_finish` is executed after a task successfully executes. The value is a dotted path, which tells Ploomber where to find your testing function. Under the hood, Ploomber will import your function and call it after the task is executed, here's some equivalent code:

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

Finally, the `transform.py` script generates a new column using `score`

```python
display_file('transform.py')
```

Let's now take a look at our tests:

```python
display_file('integration_tests.py')
```

## Testing Python scripts

To test your Python scripts, you have to know which file to look at. You can do so by simply adding `product` as argument to your function. If your Python script generates more than one product (like in our case), `product` will be a dictionary-like object, that's why we are using `product['data']`. This returns a `Product` object, to get the path to the file, simply use the `str` function.

```pycon
>>> product # dictionary-like object: maps names to Product objects
>>> product['data'] # Product object
>>> str(product['data']) # path to the data file
```

## Testing SQL scripts

To test SQL scripts, you also need the client to send queries to the appropriate database, to do so, just add `client` to your testing function.

The `ploomber.testing.sql` module implements convenient functions to test your tables. They always take `client` as its first argument, just pass the client variable directly. Since our SQL script only generates a product, you can directly pass the product object to the testing function (otherwise pass `product[key]`) with the appropriate key.

*Note:* If you're implementing your own SQL testing logic, doing `str(product)` will return a `{schema}.{name}` string, you can also use `product.schema` and `product.name`.

## Running the pipeline

Let's now run our pipeline:

```sh
ploomber build
```

Everything looks good.

Let's now imagine a colleague found an error in the cleaning logic and has re-written the script. However, he was unaware that both columns in the raw table had corrupted data and forgot to include the filtering conditions.

The script now looks like this:

```python
path = Path('clean.sql')
new_code = path.read_text().replace('WHERE score is not null AND age > 0', '')
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

Ploomber error messages are designed to give you enough context, so you can fix things quickly.

The last line says that our pipeline failed to build:

```
ploomber.exceptions.DAGBuildError: Failed to build DAG
```

That's a very general error message, but it tells us at which stage our pipeline failed (building is not the only one). If you go up a few lines, you'll see this:

```
ploomber.exceptions.TaskBuildError: Exception when running on_finish for task "clean"
```

That's a bit more specific. It's pointing us to the `on_finish` hook in the `clean` task. Go up a few more lines:

```
assert not nulls_in_columns(client, ['score', 'age'], product)
AssertionError
```

That tells me the exact test that failed! While having this long error messages might seem to verbose, it helps a lot to understand why the pipeline failed, our take away from the error message is: "the pipeline building process failed because the `on_finish` hook in the `clean` task raised an exception in this line". That's much better than either "the pipeline failed" or "this line raised an exception".

Let's fix our pipeline and add the `WHERE` clause again:

```python
path = Path('clean.sql')
new_code = path.read_text() + 'WHERE score is not null AND age > 0'
path.write_text(new_code)
display_file('clean.sql')
```

```sh
ploomber build
```

<!-- #region -->
All good! Pipeline is running without issues again!

## Test-driven development (TDD)

Writing data tests is essential for developing robust pipelines. Coding tests is simple, all we have to do is write in code that we already have in our mind when thinking what the outcome of a script should be.

This thought process happens *before* we write the actual code, which means we could easily write tests even before we write the actual code. This approach is called Test-driven development (TDD).

Following this framework has an added benefit, since we force ourselves to put in concrete terms our data expectations, it makes easier to think how we want to get there.

Furthermore, *tests also serve as documentation* for us (and for others). By looking at our tests, anyone can see what *our intent* is. Then by looking at the code, it will be easier to spot mismatches between our intent and our implementation.


## Pro tip: debugging and developing tests interactively

Even though tests are usually just a few short statements, writing them in an interactive way can help you quickly prototype your assertions. One simple trick you can use to do this is to start an interactive session and load the `client` and `product` variables.

Let's imagine you want to write a test for a new SQL script (but the same applies for other types of scripts). You add a testing function, but it's currently empty:

```python
def my_sql_testing_function(client, product):
    pass
```

If you run this, Ploomber will still call your function, you can start an interactive session when this happens:

```python
def my_sql_testing_function(client, product):
    from IPython import embed; embed()
```

Once you call `ploomber build`, wait for the Python prompt to show and verify you have the `client` and `product` variables:

```pycon
>>> print(client)
>>> print(product)
```


## Where to go next

* [Documentation for ploomber.testing - Handy functions for testing pipelines](../api/testing.rst)
* [Our blog post on CI for Data Science (which includes a section on testing pipelines)](https://towardsdatascience.com/rethinking-continuous-integration-for-data-science-ebf0dfc61788)
<!-- #endregion -->
