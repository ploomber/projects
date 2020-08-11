```python
from pathlib import Path
from IPython.display import Markdown, display
```

```python
def print_file(path):
    path = Path(path)
    kind = path.suffix.replace('.', '')
    content = path.read_text()
    display(Markdown("""
```{}
{}
```
""".format(kind, content)))
```

```python
print_file('pipeline.yaml')
```

```python
print_file('sql/create-table.sql')
```

```python
print_file('sql/macros.sql')
```

```python
! ploomber task sql-task --source
```
