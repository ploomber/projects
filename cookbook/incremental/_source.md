---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Incremental processing

<!-- start description -->
A pipeline that processes new records from a database and uploads them.
<!-- end description -->


A common scenario is to have a pipeline that processes records incrementally. For example, we might load data from a data warehouse, process all historical records one, and store results in another table. However, when running the pipeline again, we might want to process new records only, since it'd be time consuming to process all records again.

To achieve so, we can add a dynamic parameter to our pipeline to return the index of the latest processed record. Let's look at the `pipeline.yaml`:

<% expand('pipeline.yaml') %>


The first task (`tasks/load.py`) has a dynamic parameter (`params::get_index`). Whenever Ploomber runs your pipeline, it'll import `params.py`, call `get_index()` and assign the returned value to the `index` parameter in the task.

Let's look at `params.py`:

<% expand('params.py') %>

You can see that it loads the parameter from an `index.json` file; however, you can store the parameter anywhere you want.

Let's now create a sample database and insert 100 records to a table named `numbers`:

```bash
# clean up data and parameters in case we have anything
rm -f data.db index.json
```

```bash
# create database and insert 100 rows
python insert.py
```

```bash
# count rows in the table
python count.py
```

Let's run the pipeline. Our tasks will load all unprocessed records from the `numbers` table, transform the data and store the output in the `plus_one` table:

```bash
ploomber build --log info --force
```

Let's check the table counts:

```bash
python count.py
```

Great, our pipeline processed the existing 100 rows in `numbers` and stored the results in the `plus_one` table.

Let's add another 100 rows to the `numbers` table:

```bash
python insert.py
```

```bash
python count.py
```

Process the data again:

```bash
ploomber build --log info --force
```

```bash
python count.py
```

Now our `plus_one` table has 200 records, and the last execution only processed 100 rows. Note that if we run the pipeline again, it'll stop after running the `load` task since there are no records to process.

```bash
ploomber build --force
```

```bash
python count.py
```
