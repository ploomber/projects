import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = None
product = {'nb': 'output/get-actions.html', 'data': 'output/actions.parquet'}

# +
n_actions = np.random.randint(1, 100, size=1000)
df = pd.DataFrame({'id': np.repeat(np.arange(1000), n_actions)})
df.to_parquet(product['data'], index=False)