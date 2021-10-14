<!-- start header -->
To run this example locally, execute: `ploomber examples -n cookbook/sql-dump`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/sql-dump%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/sql-dump%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

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