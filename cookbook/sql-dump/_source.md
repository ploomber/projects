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

# SQLDump example

A minimal example to dump from a SQL database using SQLDump.

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