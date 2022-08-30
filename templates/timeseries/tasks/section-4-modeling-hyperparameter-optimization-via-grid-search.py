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
import warnings
import itertools
import statsmodels.api as sm
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['section-2-preprocess-data']
product = None

# %% tags=["soorgeon-unpickle"]
y = pickle.loads(Path(upstream['section-2-preprocess-data']['y']).read_bytes())

# %% [markdown]
# ## 4 Modeling: Hyperparameter optimization via grid search

# %% [markdown]
# _The following is from https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3_.
#
# > There are three distinct integers `p`, `d`, `q` that are used to parametrize ARIMA models. Because of that, ARIMA models are denoted with the notation `ARIMA(p, d, q)`. Together these three parameters account for seasonality, trend, and noise in datasets.
# > 
# > - `p` is the auto-regressive part of the model. It allows us to incorporate the effect of past values into our model. Intuitively, this would be similar to stating that it is likely to be warm tomorrow if it has been warm the past 3 days.
# > - `d` is the integrated part of the model. This includes terms in the model that incorporate the amount of differencing (i.e. the number of past time points to subtract from the current value) to apply to the time series. Intuitively, this would be similar to stating that it is likely to be same temperature tomorrow if the difference in temperature in the last three days has been very small.
# > - `q` is the moving average part of the model. This allows us to set the error of our model as a linear combination of the error values observed at previous time points in the past.
# > 
# > When dealing with seasonal effects, we make use of the seasonal ARIMA, which is denoted as `ARIMA(p,d,q)(P,D,Q)s`. Here, `p`, `d`, `q` are the non-seasonal parameters described above, while `P`, `D`, `Q` follow the same definition but are applied to the seasonal component of the time series. The term `s` is the periodicity of the time series (4 for quarterly periods, 12 for yearly periods, etc.).
#
# We're using grid search to find the params.

# %%
# Define p, d, q params to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, d, q
pdq = list(itertools.product(p, d, q))

# Generate all different combos of seasonal P, D, Q
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

# %%
print('Examples of parameter combos for SARIMA:')
print('SARIMA: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMA: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMA: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMA: {} x {}'.format(pdq[2], seasonal_pdq[4]))

# %% [markdown]
# The following grid search optimizes the params for best (lowest) [AIC](https://en.wikipedia.org/wiki/Akaike_information_criterion):

# %%
warnings.filterwarnings("ignore")

# The blog post doesn't separate the training and test sets.
# I'm doing that here. Everything up to 1997-12-31 is training.
#y_trunc = y[:'1997-12-31']

min_aic = float('inf')
min_params = None
min_params_seasonal = None
min_model = None

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(
#                y_trunc,
                y,
                order=param,
                seasonal_order=param_seasonal,
                enforce_stationarity=False,
                enforce_invertibility=False)
            results = mod.fit()
            if results.aic < min_aic:
                min_aic = results.aic
                min_params = param
                min_params_seasonal = param_seasonal
                min_model = results
            print('ARIMA{}x{}: aic={}'.format(param, param_seasonal, results.aic))
        except:
            continue

# %%
print('min_aic={}, min_params={}, min_params_seasonal={}'.format(min_aic, min_params, min_params_seasonal))

# %% tags=["soorgeon-pickle"]
Path(product['min_model']).parent.mkdir(exist_ok=True, parents=True)
Path(product['min_model']).write_bytes(pickle.dumps(min_model))

Path(product['results']).parent.mkdir(exist_ok=True, parents=True)
Path(product['results']).write_bytes(pickle.dumps(results))
