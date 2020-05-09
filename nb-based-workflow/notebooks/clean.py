# + tags=[]
import pandas as pd

# + tags=["parameters"]
product = None
upstream = None

# + tags=[]
df = pd.read_csv(upstream['load.py']['data'])

df

df['x'] = df['x'] + 2

df.to_csv(product['data'], index=False)
