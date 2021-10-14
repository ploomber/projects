# Clean actions data
import pandas as pd

# + tags=["parameters"]
upstream = ['get-actions']
product = {
    'nb': 'output/clean-actions.ipynb',
    'data': 'output/clean-actions.parquet'
}
# -

df = pd.read_parquet(upstream['get-actions']['data'])
df.to_parquet(product['data'], index=False)
