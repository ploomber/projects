import pandas as pd
import numpy as np

# + tags=['parameters']
product = None

# +
df = pd.DataFrame({'x': np.random.rand(100)})

df.to_csv(product['data'], index=False)

df

print('new cell')

print('brand new cell')
