# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# **Important**: *@capture is an experimental API*

# %%
from ploomber.inline import dag_from_functions, grid, capture

import pandas as pd
from sklearn_evaluation import plot
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.metrics import accuracy_score

from sklearn_evaluation import NotebookCollection, NotebookDatabase
from glob import glob


# %%
def get():
    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])

    df.columns = d['feature_names']
    df['target'] = d['target']
    return df

@grid(model=[ExtraTreesClassifier, RandomForestClassifier, AdaBoostClassifier],
      n_estimators=[5, 10],
      criterion=['gini', 'entropy'])
@capture
def fit(get, model, n_estimators):
    X = get.drop('target', axis='columns')
    y = get.target
    
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)
    clf = model(n_estimators=n_estimators)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    # tag=features
    list(get.columns)
    
    # tag=model
    model.__name__
    
    # tag=params
    clf.get_params()
    
    # tag=plot
    plot.confusion_matrix(y_test, y_pred)
    
    # tag=accuracy
    accuracy_score(y_test, y_pred)
    
    return clf


# %%
# # %%capture
dag = dag_from_functions([get, fit], parallel=True,
                         output='cache-ml')
# dag.plot()

# %%
# # %%capture
dag.build(force=True)

# %%
clf = dag['fit-4'].load(key='return')
clf

# %%
collection = NotebookCollection(glob('cache-ml/*.ipynb'))

# %%
collection['params']

# %%
collection['plot']

# %%
db = NotebookDatabase('nb.db', 'cache-ml/*.ipynb')
db.index()

# %%
# %load_ext sql

# %% magic_args="sqlite:///nb.db" language="sql"
# SELECT
#     path,
#     json_extract(c, '$.model') AS model,
#     json_extract(c, '$.params.criterion') AS criterion,
#     json_extract(c, '$.params.n_estimators') AS n_estimators,
#     json_extract(c, '$.accuracy') AS accuracy
# FROM nbs
# ORDER BY 5 DESC
# LIMIT 5

# %% magic_args="sqlite:///nb.db" language="sql"
# SELECT
#     path,
#     json_extract(c, '$.model') AS model,
#     json_extract(c, '$.params.criterion') AS criterion,
#     json_extract(c, '$.params.n_estimators') AS n_estimators,
#     json_extract(c, '$.accuracy') AS accuracy
# FROM nbs
# WHERE model = 'AdaBoostClassifier'
# ORDER BY 5 DESC

# %%
