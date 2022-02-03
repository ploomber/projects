# %%
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# %% tags=["parameters"]
upstream = ['load']
product = None



# %%
def my_preprocessing_function(X_train, X_test):
    encoder = OneHotEncoder()
    X_train_t = encoder.fit_transform(X_train)
    X_test_t = encoder.transform(X_test)
    return X_train_t, X_test_t


# %%
X_train = pd.read_csv(upstream['load']['train'])
X_test = pd.read_csv(upstream['load']['test'])

# %%
my_preprocessing_function(X_train, X_test)
