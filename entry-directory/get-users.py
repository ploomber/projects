import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = None
product = {'nb': 'output/get-users.html', 'data': 'output/users.parquet'}

df = pd.DataFrame({
    'id': np.arange(1000),
    'age': np.random.normal(loc=30, scale=10, size=1000)
})

df.to_parquet(product['data'], index=False)