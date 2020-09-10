import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = ['clean-users', 'clean-actions']
product = {
    'nb': 'output/model-evaluation.ipynb',
    'model': 'output/model.pickle'
}

# +
df = pd.read_parquet(upstream['clean-users']['data'])
df.to_parquet(product['model'], index=False)
