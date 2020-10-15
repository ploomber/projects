__version__ = '0.1'

from pathlib import Path
from IPython.display import Markdown, display
from ploomberutils.nb import process_readme


def display_file(path, syntax=None):
    path = Path(path)

    kind = path.suffix.replace('.', '')

    # pygments (used for syntax highlighting in the docs) does no work
    # if we set sql and have jinja placeholders, but postgresql works!
    if kind == 'sql':
        kind = 'postgresql'

    content = path.read_text()
    display(Markdown("""
```{}
{}
```
""".format(syntax or kind, content)))


def filter_output(captured, startswith):
    return print('\n'.join([
        line for line in captured.stderr.split('\n')
        if line.startswith(startswith)
    ]))


__all__ = ['display_file', 'process_readme']
