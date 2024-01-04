<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/sql-dump`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/sql-dump/README.ipynb)
<!-- end header -->



# SQLDump example

<!-- start description -->
A minimal example showing how to dump a table from a SQL database.
<!-- end description -->

Create some sample data:

```python
from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame({'numbers': range(10)})

engine = create_engine('sqlite:///my.db')

df.to_sql('my_numbers', engine, if_exists='replace')
```

Dump data:

```sh
ploomber build
```
