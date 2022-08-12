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
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['split']
product = None

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
product = {"nb": "/home/jovyan/onboarding/output/random-forest.ipynb"}


# %% tags=["soorgeon-unpickle"]
X_test = pickle.loads(Path(upstream['split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['split']['X_train']).read_bytes())
y_test = pickle.loads(Path(upstream['split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['split']['y_train']).read_bytes())

# %% [markdown] tags=[]
# ## Random Forest

# %% tags=["plot"]
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
sns.scatterplot(x=y_test.flatten(), y=y_pred)

# %%
print('RMSE for Random Forest Regressor=>',np.sqrt(mean_squared_error(y_test, y_pred)))
