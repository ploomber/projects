# Clean actions data

import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = ['get-actions']
product = {
    'nb': 'output/clean-actions.html',
    'data': 'output/clean-actions.parquet'
}

# +
df = pd.read_parquet(upstream['get-actions']['data'])
df.to_parquet(product['data'], index=False)