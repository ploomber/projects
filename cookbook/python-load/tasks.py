from pathlib import Path


def create_file(product):
    Path(product).touch()