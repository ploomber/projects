__version__ = '0.1'

from functools import reduce
from pathlib import Path

from IPython.display import Markdown, display
import parso

from ploomberutils.nb import process_readme_md

# pygments (used for syntax highlighting in the docs) does not work
# if we set sql and have jinja placeholders, but postgresql works!
_SYNTAX_MAP = {
    'sql': 'postresql',
}


def display_file(path, syntax=None, symbols=None, lines=None):
    """Display file in Jupyter

    Parameters
    ----------
    path : str
        Path to file

    syntax : str, default=None
        Syntax to use, if None it uses the extension in the path argument

    symbols : list, default=None
        List of symbols from the file to display. If None, it displays the
        complete file.
    """
    path = Path(path)

    suffix = path.suffix.replace('.', '')

    syntax = syntax or suffix

    if syntax in _SYNTAX_MAP:
        syntax = _SYNTAX_MAP[syntax]

    content = path.read_text()

    if symbols:
        content = _get_symbols(content, symbols)

    content = content.strip()

    if lines:
        # convert to zero based index
        first, last = (lines[0] - 1, lines[1] - 1)
        content = '\n'.join(content.splitlines()[first:last])

    display(Markdown("""
```{}
{}
```
""".format(syntax, content)))


def _process_node(node):
    if hasattr(node, 'name'):
        return node.name.value
    elif node.type == 'decorated':
        return node.children[-1].name.value
    else:
        raise RuntimeError


def _get_symbols(content, symbols):
    """
    Extract symbols from a string with Python code
    """
    module = parso.parse(content)

    named = {
        _process_node(c): c.get_code().strip()
        for c in module.children if hasattr(c, 'name') or c.type == 'decorated'
    }

    if isinstance(symbols, str):
        content_selected = named[symbols]
    else:
        content_selected = '\n\n\n'.join([named[s] for s in symbols])

    # content_selected contains the requested symbols, let's now subset the
    # imports so we only display the ones that are used

    # build a defined-name -> import-statement-code mapping. Note that
    # the same code may appear more than once if it defines more than one name
    # e.g. from package import a, b, c
    imports = [{
        name.value: import_.get_code().rstrip()
        for name in import_.get_defined_names()
    } for import_ in module.iter_imports()]
    imports = reduce(lambda x, y: {**x, **y}, imports)

    # parse the selected content to get the used symbols
    leaf = parso.parse(content_selected).get_first_leaf()
    # store used symbols here
    names = []

    while leaf:
        if leaf.type == 'name':
            names.append(leaf.value)

        leaf = leaf.get_next_leaf()

    # iterate over names defined by the imports and get the import statement
    # if content_subset uses it
    imports_to_use = []

    for name, import_code in imports.items():
        if name in names:
            imports_to_use.append(import_code)

    # remove duplicated elements but keep order, then join
    imports_to_use = '\n'.join(list(dict.fromkeys(imports_to_use)))

    return f'{imports_to_use}\n\n\n{content_selected}'


def filter_output(captured, startswith):
    return print('\n'.join([
        line for line in captured.stderr.split('\n')
        if line.startswith(startswith)
    ]))


__all__ = ['display_file', 'process_readme_md']
