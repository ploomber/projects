from pathlib import Path


import joblib
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier


def get(product, sample_frac):
    """Get data
    """
    d = datasets.load_iris()

    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']

    # for running tests
    if sample_frac:
        df = df.sample(frac=sample_frac)

    df.to_parquet(str(product))


def features(upstream, product):
    """Generate new features from existing columns
    """
    data = pd.read_parquet(str(upstream['get']))
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    df = pd.DataFrame({'sepal area (cm2)': ft})
    df.to_parquet(str(product))


def join(upstream, product):
    """Join raw data with generated features
    """
    a = pd.read_parquet(str(upstream['get']))
    b = pd.read_parquet(str(upstream['features']))
    df = a.join(b)
    df.to_parquet(str(product))


def fit(upstream, product):
    """Fit model and generate classification report
    """
    df = pd.read_parquet(str(upstream['join']))
    X = df.drop('target', axis='columns')
    y = df.target

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.33,
                                                        random_state=42)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred)

    Path(str(product['report'])).write_text(report)
    joblib.dump(clf, str(product['model']))
