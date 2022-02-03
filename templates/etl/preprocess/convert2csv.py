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
import xml2csv

# %% tags=["parameters"]
upstream = None
product = None

# %%
Path(product['data']).mkdir(exist_ok=True)

# %%
for f in Path(upstream['download']['extracted']).glob('*'):
    print(f)
    out = Path(product['data'], f.name.replace('.xml', '.csv'))
    xml2csv.convert(f, out)
