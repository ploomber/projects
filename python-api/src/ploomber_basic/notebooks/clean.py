import pandas as pd

# + tags=["parameters"]
product = None
upstream = None

# +
df = pd.read_csv(upstream['load'])
df

# +
df['x'] = df['x'] + 1
df.to_csv(product['data'], index=False)
