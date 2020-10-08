# Train model and evaluate

# +
import pickle

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# +
plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['font.size'] = 20

# + tags=["parameters"]
upstream = ['clean-users', 'clean-actions']
product = {
    'nb': 'output/model-evaluation.ipynb',
    'model': 'output/model.pickle'
}
# -

users = pd.read_parquet(upstream['clean-users']['data'])
actions = pd.read_parquet(upstream['clean-actions']['data'])

users.head()

actions.head()

actions_count = pd.DataFrame({'n_actions': actions.groupby('id').size()})
actions_count.head()

df = users.merge(actions_count, on=['id']).set_index('id')
df.head()

# just for sake of example: define target variable using input features with
# some added noise
y = 0.2 * df.age + df.n_actions + np.random.normal(10, 10, len(df)) > 50

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.20)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

plot_confusion_matrix(clf, X_test, y_test)

with open(product['model'], 'wb') as f:
    pickle.dump(clf, f)
