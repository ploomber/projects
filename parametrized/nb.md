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
print_file('print.py')
```

```python
! ploomber build --help
```

```python
%%capture captured
! ploomber build --force --log INFO
```

```python
def print_papermill_output(captured):
    return print('\n'.join([l for l in captured.stdout.split('\n') if l.startswith('INFO:papermill:some_param')]))
```

```python
print_papermill_output(captured)
```

```python
%%capture captured
! ploomber build --force --env__some_param another_value --log INFO
```

```python
print_papermill_output(captured)
```

```python
! tree output
```
