# %%
import pickle

# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

# %% tags=["parameters"]
upstream = ['features']
product = None
model_type = 'random-forest'
n_estimators = None
criterion = None
learning_rate = None

# %%
df = pd.read_csv(str(upstream['features']))
X = df.drop('target', axis='columns')
y = df.target

# %%
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)

# %%
if model_type == 'random-forest':
    clf = RandomForestClassifier(n_estimators=n_estimators,
                                 criterion=criterion)
elif model_type == 'ada-boost':
    clf = AdaBoostClassifier(n_estimators=n_estimators,
                             learning_rate=learning_rate)
else:
    raise ValueError(f'Unsupported model type: {model_type!r}')

# %%
clf.fit(X_train, y_train)

# %%
y_pred = clf.predict(X_test)

# %%
print(classification_report(y_test, y_pred))

# %%
with open(product['model'], 'wb') as f:
    pickle.dump(clf, f)
