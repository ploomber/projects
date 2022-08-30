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
# ### 6.2 Dynamic forecasts

# %%
pred_dynamic = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()

# %%
ax = y['1990':].plot(label='observed', figsize=(15, 6))
pred_dynamic.predicted_mean.plot(label='Dynamic Forecast', ax=ax)

ax.fill_between(
    pred_dynamic_ci.index,
    pred_dynamic_ci.iloc[:, 0],
    pred_dynamic_ci.iloc[:, 1],
    color='k',
    alpha=.25)

ax.fill_betweenx(
    ax.get_ylim(),
    pd.to_datetime('1998-01-01'),
    y.index[-1],
    alpha=.1,
    zorder=-1)

ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')

plt.legend()
plt.show()

# %%
# Extract the predicted and true values of our time series
y_forecasted = pred_dynamic.predicted_mean
y_truth = y['1998-01-01':]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
