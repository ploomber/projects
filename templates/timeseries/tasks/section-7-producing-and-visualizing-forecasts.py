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
# ## 7 Producing and visualizing forecasts

# %%
# Get forecast 500 steps ahead in future
pred_uc = results.get_forecast(steps=500)

# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()

# %%
ax = y.plot(label='observed', figsize=(15, 8))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')

plt.legend()
plt.show()
