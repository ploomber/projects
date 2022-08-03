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
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['split']
product = None

# %% tags=["soorgeon-unpickle"]
X = pickle.loads(Path(upstream['split']['X']).read_bytes())
y = pickle.loads(Path(upstream['split']['y']).read_bytes())

# %% [markdown]
# ## Polynomial Regression

# %%
###################### Polynomial Regression #######################################
poly = PolynomialFeatures(degree =4) 
X_poly = poly.fit_transform(X) 
poly.fit(X_poly, y) 

lin2 = LinearRegression() 
lin2.fit(X_poly, y) 
pred = lin2.predict(X_poly)
new_X, new_y = zip(*sorted(zip(X, pred)))

# poly.fit(X_train, y_train) 
# lin2.fit(X_train, y_train) 
# y_pred = lin2.predict(X_test)
# new_X, new_y = zip(*sorted(zip(X_test, y_pred)))


plt.figure(figsize=(16, 8))
plt.scatter(
    X,
    y,
    c='black'
)
plt.plot(
    new_X, new_y,
    c='blue'
)
plt.xlabel("Tests")
plt.ylabel("Cases")
plt.show()
# RMSE for Linear Regression=> 131.07677569045717
print('RMSE for Linear Regression=>',np.sqrt(mean_squared_error(y,lin2.predict(poly.fit_transform(X)))))
