<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/incremental`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/incremental/README.ipynb)
<!-- end header -->



# Incremental processing

<!-- start description -->
A pipeline that processes new records from a database and uploads them.
<!-- end description -->


A common scenario is to have a pipeline that processes records incrementally. For example, we might load data from a data warehouse, process all historical records one, and store results in another table. However, when running the pipeline again, we might want to process new records only, since it'd be time consuming to process all records again.

To achieve so, we can add a dynamic parameter to our pipeline to return the index of the latest processed record. Let's look at the `pipeline.yaml`:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: tasks/load.py
    product:
      nb: output/load.ipynb
      data: output/raw.csv
    params:
      index: 
        dotted_path: params::get_index
        path_to_index: '{{root}}/index.json'

      path_to_db: '{{root}}/data.db'

    on_finish: hooks.check_if_new_records

  - source: tasks/process.py
    product:
      nb: output/process.ipynb
      data: output/processed.csv

  - source: tasks/upload.py
    product:
      nb: output/upload.ipynb
    params:
      path_to_db: '{{root}}/data.db'

    on_finish:
      dotted_path: hooks.store_index
      path_to_index: '{{root}}/index.json'
```
<!-- #endmd -->


The first task (`tasks/load.py`) has a dynamic parameter (`params::get_index`). Whenever Ploomber runs your pipeline, it'll import `params.py`, call `get_index()` and assign the returned value to the `index` parameter in the task.

Let's look at `params.py`:

<!-- #md -->
```python
# Content of params.py
import json
from pathlib import Path


def get_index(path_to_index):
    path = Path(path_to_index)

    if not path.exists():
        return -1

    index = json.loads(path.read_text())
    return index['latest']

```
<!-- #endmd -->

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