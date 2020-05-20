# + tags=[]
import pandas as pd

# + tags=["parameters"]
product = None
upstream = None

# + tags=[]
df = pd.read_csv(upstream['load'])
df
# + tags=[]
df['x'] = df['x'] + 1
df.to_csv(product['data'], index=False)

# + tags=[]