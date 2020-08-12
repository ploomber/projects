__version__ = '0.1'

from pathlib import Path
from IPython.display import Markdown, display


def display_file(path):
    path = Path(path)
    kind = path.suffix.replace('.', '')
    content = path.read_text()
    display(Markdown("""
```{}
{}
```
""".format(kind, content)))


def filter_output(captured, startswith):
    return print('\n'.join([
        line for line in captured.stderr.split('\n')
        if line.startswith(startswith)
    ]))
