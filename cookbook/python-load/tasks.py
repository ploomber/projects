# %%
from pathlib import Path


# %%
def create_file(product):
    Path(product).touch()


# %%
def create_another(upstream, product):
    text = Path(upstream['create_file']).read_text()
    Path(product).write_text(text)


# %%
def create_final(upstream, product):
    text = Path(upstream['create_another']).read_text()
    Path(product).write_text(text)
