# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=[]
import importlib
import pickle
from pathlib import Path

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
import pandas as pd

# %% tags=["parameters"]
upstream = ['load']
product = None


# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
model = "sklearn.ensemble.RandomForestClassifier"
model_params = {"n_estimators": [2, 5]}
upstream = {
    "load": {
        "nb": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/products/load.html",
        "data": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/data.csv",
    }
}
product = {
    "nb": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/products/fit-0.html",
    "model": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/model-0.pkl",
}


# %%
df = pd.read_csv(upstream['load']['data'])

X = df.drop('target', axis='columns')
y = df.target

# %% tags=[]
mod, _, name = model.rpartition('.')

# %% tags=[]
CLASS = getattr(importlib.import_module(mod), name)

# %% tags=[]
clf = CLASS()
clf

# %% tags=[]
clf_grid = GridSearchCV(clf, param_grid=model_params)

# %% tags=[]
cv = cross_validate(clf_grid, X, y, scoring='accuracy', cv=3)
scores = ' + '.join(f'{s:.2f}' for s in cv["test_score"])
mean_ = cv["test_score"].mean()

# %% tags=[]
print(f'Cross-validated accuracy: ({scores}) / 3 = {mean_:.2f}')

# %%
clf_grid.fit(X, y)

# %%
best = clf_grid.best_estimator_

# %%
Path(product['model']).write_bytes(pickle.dumps(best))

# %%
