# SQLDump example

A minimal example to dump from a SQL database using SQLDump.

Create some sample data:

```python
from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame({'numbers': range(10)})

engine = create_engine('sqlite:///my.db')

df.to_sql('my_numbers', engine)
```

Dump data:

```sh
ploomber build
```