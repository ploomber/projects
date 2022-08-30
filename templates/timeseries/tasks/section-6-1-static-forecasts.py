# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
# ---

# %% tags=["soorgeon-imports"]
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['section-2-preprocess-data', 'section-5-model-fit-and-diagnostics']
product = None

# %% tags=["soorgeon-unpickle"]
y = pickle.loads(Path(upstream['section-2-preprocess-data']['y']).read_bytes())
results = pickle.loads(Path(upstream['section-5-model-fit-and-diagnostics']['results']).read_bytes())

# %% [markdown]
# ### 6.1 Static forecasts

# %%
pred = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=False)
pred_ci = pred.conf_int()

# %%
ax = y['1990':].plot(label='observed', figsize=(15, 6))
pred.predicted_mean.plot(ax=ax, label='One-step-ahead forecast', alpha=0.7)

ax.fill_between(
    pred_ci.index,
    pred_ci.iloc[:, 0],
    pred_ci.iloc[:, 1],
    color='k',
    alpha=0.2)

ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')
plt.legend()
plt.show()

# %%
y_forecasted = pred.predicted_mean
y_truth = y['1998-01-01':]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
