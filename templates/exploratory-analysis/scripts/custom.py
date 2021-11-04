# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Create custom plots.


import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

# prettier plots
plt.style.use('ggplot')
# larger plots
matplotlib.rc('figure', figsize=(15, 10))
# larger fonts
sns.set_context('notebook', font_scale=1.5)

# + tags=["parameters"]
upstream = ['clean']
product = None
# -


df = pd.read_csv(upstream['clean']['data'])

df.head()

_ = df['species'].value_counts().plot(kind='bar')

fig = px.histogram(df, x="bill_length_mm")
fig.show()

sns.pairplot(df, hue="species", height=3,diag_kind="hist")


