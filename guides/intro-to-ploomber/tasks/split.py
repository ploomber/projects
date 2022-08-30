# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
# ---

# %% tags=["soorgeon-imports"]
from sklearn.model_selection import train_test_split
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['clean']
product = None

# %% tags=["soorgeon-unpickle"]
data = pickle.loads(Path(upstream['clean']['data']).read_bytes())

# %% [markdown]
# ## Split

# %%
# plt.figure(figsize=(16, 8))
# plt.scatter(
#     data['Tests'],
#     data['Cases'],    
#     c='black'
# )
# plt.axis('scaled')
# plt.xlabel("Tests")
# plt.ylabel("Cases")
# plt.show()

X = data['Tests'].values.reshape(-1,1)
y = data['Cases'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# %% tags=["soorgeon-pickle"]
Path(product['X']).parent.mkdir(exist_ok=True, parents=True)
Path(product['X']).write_bytes(pickle.dumps(X))

Path(product['X_test']).parent.mkdir(exist_ok=True, parents=True)
Path(product['X_test']).write_bytes(pickle.dumps(X_test))

Path(product['X_train']).parent.mkdir(exist_ok=True, parents=True)
Path(product['X_train']).write_bytes(pickle.dumps(X_train))

Path(product['y']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y']).write_bytes(pickle.dumps(y))

Path(product['y_test']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y_test']).write_bytes(pickle.dumps(y_test))

Path(product['y_train']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y_train']).write_bytes(pickle.dumps(y_train))
