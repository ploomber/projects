import pandas as pd

# + tags=["parameters"]
upstream = ['dump']
product = None

# +
df = pd.read_csv(upstream['dump'])
df['multiplied_score'] = df.score * 42

# +
df.to_csv(product['data'])
