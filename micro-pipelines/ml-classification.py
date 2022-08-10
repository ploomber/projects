import warnings
warnings.filterwarnings('ignore')

# +
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn_evaluation import plot
import matplotlib.pyplot as plt

from ploomber.micro import dag_from_functions, grid


# -

# ## Declare steps

# +
def data():
    data = datasets.make_classification(1000, 10, n_informative=5,
                                        class_sep=0.80)
    X, y = data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    return X_train, X_test, y_train, y_test

def features(data):
    X_train, X_test, y_train, y_test = data
    poly = PolynomialFeatures()
    X_train_feats = poly.fit_transform(X_train)
    X_test_feats = poly.transform(X_test)
    return X_train_feats, X_test_feats, y_train, y_test, poly

def scaled(features):
    X_train, X_test, y_train, y_test, _ = features
    scaler = StandardScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm = scaler.transform(X_test)
    return X_train_norm, X_test_norm, y_train, y_test, scaler

@grid(model=[RandomForestClassifier],
      n_estimators=[50, 100, 200],
      criterion=["gini", "entropy"],
)
def fit_random_forest(scaled, model, n_estimators, criterion):    
    X_train, X_test, y_train, y_test, _ = scaled
    clf = model(n_estimators=n_estimators, criterion=criterion)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return dict(clf=clf, acc=acc)

@grid(model=[AdaBoostClassifier],
      n_estimators=[50, 100, 200],
      learning_rate=[1.0, 2.0],
)
def fit_ada_boost(scaled, model, n_estimators, learning_rate):    
    X_train, X_test, y_train, y_test, _ = scaled
    clf = model(n_estimators=n_estimators, learning_rate=learning_rate)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return dict(clf=clf, acc=acc)


# -

# ## Plot pipeline

dag = dag_from_functions([data, features, scaled, fit_random_forest, fit_ada_boost])

dag.plot()

# ## Run

dag.build()

# ## Sort models by performance

outputs = [task.load() for name, task in dag.items() if name.startswith('fit_')]

for out in sorted(outputs, key=lambda k: k['acc'], reverse=True):
    print(f'{out["clf"]}: {out["acc"]:.2f}')
