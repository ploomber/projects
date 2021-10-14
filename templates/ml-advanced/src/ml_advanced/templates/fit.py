# Script to train a model

# +
import importlib
import pickle

import pandas as pd
from sklearn.model_selection import cross_val_predict, GridSearchCV
from sklearn.metrics import classification_report
from sklearn_evaluation import plot

# + tags=["parameters"]
upstream = ['join']
product = None
model_class = None
model_params = None
# -

tokens = model_class.split('.')
module_name, class_name = '.'.join(tokens[:-1]), tokens[-1]

module_ = importlib.import_module(module_name)
class_ = getattr(module_, class_name)
clf = class_()

df = pd.read_parquet(str(upstream['join']))
X = df.drop('target', axis='columns')
y = df.target

# Perform grid search over the passed parameters
grid = GridSearchCV(clf, model_params, n_jobs=-1, cv=2)

# We want to estimate generalization performance *and* tune hyperparameters
# so we are using nested cross-validation
y_pred = cross_val_predict(grid, X, y)

print(classification_report(y, y_pred))

plot.confusion_matrix(y, y_pred)

# find best params
grid.fit(X, y)
grid.best_params_

plot.grid_search(grid.cv_results_, change=list(model_params))

best = grid.best_estimator_
best

with open(product['model'], 'wb') as f:
    pickle.dump(best, f)
