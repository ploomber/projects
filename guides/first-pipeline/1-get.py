# %%
"""
Get data
"""
import pandas as pd
from pathlib import Path

# %% tags=["parameters"]
upstream = None
product = None

# %%
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv")
df.head()

# %%
Path('output').mkdir(exist_ok=True)

df.to_csv(str(product['data']), index=False)
# %%

