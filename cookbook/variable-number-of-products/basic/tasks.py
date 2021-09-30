import shutil
from pathlib import Path
from random import randint


def _write_variable_number_of_files(parent):
    parent = Path(parent)

    # clean up products from the previous run, if any. Otherwise they'll be
    # mixed with the current files
    if parent.exists():
        shutil.rmtree(parent)

    # make sure the directory exists
    parent.mkdir(exist_ok=True, parents=True)

    # write files inside the directory
    n = randint(1, 5)
    print(f'Files to write: {n}')

    for i in range(n):
        (parent / f'{i}.txt').write_text(f'File number {i}')


def variable(product):
    """A task that generates a random number of text files
    """
    # write files
    _write_variable_number_of_files(product)


def many_products_one_variable(product):
    """
    A task that generates one file and a directory with a random number of files
    """
    # fixed (one file)
    Path(product['one']).write_text('one')

    # variable (many files)
    _write_variable_number_of_files(product['variable'])


def variable_downstream(product, upstream):
    """A task that reads the variable number of files from "variable"
    """
    directory = Path(upstream['variable'])
    content = '\n'.join([Path(p).read_text() for p in directory.glob('*')])
    Path(product).write_text(content)


def many_products_one_variable_downstream(product, upstream):
    """
    A task that reads the variable number of files
    from "many_products_one_variable"
    """
    directory = Path(upstream['many_products_one_variable']['variable'])
    content = '\n'.join([Path(p).read_text() for p in directory.glob('*')])
    Path(product).write_text(content)
