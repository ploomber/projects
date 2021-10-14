"""
Clean
"""
import pandas as pd

# + tags=["parameters"]
upstream = ['get']
product = None
# -

df = pd.read_csv(upstream['get']['data'])
# data cleaning code...

df.to_csv(str(product['data']), index=False)
