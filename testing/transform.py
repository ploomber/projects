import pandas as pd

# + tags=["parameters"]
upstream = ['dump']
product = None

# +
df = pd.read_csv(upstream['dump'])
df['derived_value'] = df.some_value * 42

# +
df.to_csv(product['data'])
