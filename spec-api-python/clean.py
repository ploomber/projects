"""
Clean
"""
import pandas as pd

# + tags=["parameters"]
upstream = ['raw']
product = None
# -

df = pd.read_csv(upstream['raw']['data'])
# data cleaning code...

df.to_csv(str(product['data']), index=False)
