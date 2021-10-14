from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


def logistic_reg():
    return Pipeline([('scaler', StandardScaler()),
                     ('clf', LogisticRegression(solver='liblinear'))])


def svc():
    return Pipeline([('scaler', StandardScaler()), ('clf', SVC())])
