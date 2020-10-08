# Get users data and make some charts

import pandas as pd
import numpy as np
import seaborn as sns

# + tags=["parameters"]
upstream = None
product = {'nb': 'output/get-users.ipynb', 'data': 'output/users.parquet'}
# -

df = pd.DataFrame({
    'id': np.arange(1000),
    'age': np.random.normal(loc=30, scale=10, size=1000)
})

sns.distplot(df.age)

df.to_parquet(product['data'], index=False)
