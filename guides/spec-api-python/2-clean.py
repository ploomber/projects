"""
Clean
"""
import pandas as pd

# + tags=["parameters"]
upstream = ['1-get']
product = None
# -

df = pd.read_csv(upstream['1-get']['data'])
# data cleaning code...

df.to_csv(str(product['data']), index=False)
