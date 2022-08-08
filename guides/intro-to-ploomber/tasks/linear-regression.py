# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=["soorgeon-imports"]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['split']
product = None
fit_intercept = None

# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
upstream = {
    "split": {
        "X_test": "/home/jovyan/onboarding/output/split-X_test.pkl",
        "y_test": "/home/jovyan/onboarding/output/split-y_test.pkl",
        "y_train": "/home/jovyan/onboarding/output/split-y_train.pkl",
        "y": "/home/jovyan/onboarding/output/split-y.pkl",
        "X": "/home/jovyan/onboarding/output/split-X.pkl",
        "X_train": "/home/jovyan/onboarding/output/split-X_train.pkl",
        "nb": "/home/jovyan/onboarding/output/split.ipynb",
    }
}
product = {"nb": "/home/jovyan/onboarding/output/linear-regression.html"}


# %% tags=["soorgeon-unpickle"]
X = pickle.loads(Path(upstream['split']['X']).read_bytes())
X_test = pickle.loads(Path(upstream['split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['split']['X_train']).read_bytes())
y = pickle.loads(Path(upstream['split']['y']).read_bytes())
y_test = pickle.loads(Path(upstream['split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['split']['y_train']).read_bytes())

# %% [markdown] tags=[]
# ## Linear regression
# In here we can see a plot of number of cases and the predictions

# %% tags=[]
print(fit_intercept)
if fit_intercept:
    reg = LinearRegression(fit_intercept=fit_intercept)
else:
    reg = LinearRegression()
# reg.fit(X, y)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

actvspred = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

plt.figure(figsize=(16, 8))
plt.scatter(
    X,
    y,
    c='black'
)
plt.plot(
    X_test,
    y_pred,
    c='blue',
    linewidth=2
)
plt.xlabel("Tests")
plt.ylabel("Cases")
plt.show()

print('RMSE for Linear Regression=>',np.sqrt(mean_squared_error(y_test, y_pred)))
