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
print("I'm loading some data...")

path = Path(product['data'])
path.write_text("""\
x,y
1,1
2,2
3,3
""")