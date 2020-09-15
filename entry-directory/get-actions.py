# Get actions data and make some charts

import pandas as pd
import numpy as np
import seaborn as sns

# + tags=["parameters"]
upstream = None
product = {'nb': 'output/get-actions.ipynb', 'data': 'output/actions.parquet'}
# -

n_actions = np.random.randint(1, 100, size=1000)
df = pd.DataFrame({'id': np.repeat(np.arange(1000), n_actions)})

sns.distplot(df.groupby('id').size())

df.to_parquet(product['data'], index=False)
