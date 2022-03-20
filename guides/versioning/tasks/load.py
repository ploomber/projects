# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path

# %% tags=["parameters"]
upstream = None
product = None


# %%
Path(product['data']).parent.mkdir(exist_ok=True, parents=True)
Path(product['data']).write_text("""\
name, x
a, 1
b, 2
c, 2
d, 3
""")
