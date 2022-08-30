# %%
from pathlib import Path


# %%
def do_something(product, crash):
    if crash:
        raise ValueError('crashed on purpose!')

    Path(product).touch()
