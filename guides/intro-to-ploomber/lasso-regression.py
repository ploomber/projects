# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
# ---

# %% tags=["soorgeon-imports"]
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['split']
product = None

# %% tags=["soorgeon-unpickle"]
X_test = pickle.loads(Path(upstream['split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['split']['X_train']).read_bytes())
y_test = pickle.loads(Path(upstream['split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['split']['y_train']).read_bytes())

# %% [markdown] tags=[]
# ## Lasso regression

# %%


lasso = linear_model.Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)
sns.scatterplot(x=y_test.flatten(), y=y_pred)
print('RMSE for Lasso Regressor=>',np.sqrt(mean_squared_error(y_test, y_pred)))
