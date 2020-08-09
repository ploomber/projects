# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from pathlib import Path
import xml2csv

# + tags=["parameters"]
upstream = None
product = None
# -

Path(product['data']).mkdir(exist_ok=True)

for f in Path(upstream['download']['extracted']).glob('*'):
    print(f)
    out = Path(product['data'], f.name.replace('.xml', '.csv'))
    xml2csv.convert(f, out)
