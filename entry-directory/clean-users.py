# Clean users data

import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = ['get-users']
product = {
    'nb': 'output/clean-users.html',
    'data': 'output/clean-users.parquet'
}

# +
df = pd.read_parquet(upstream['get-users']['data'])
df.to_parquet(product['data'], index=False)