# +
from imdb_project import pipeline

import pandas as pd
# -

dag = pipeline.make()

import logging
logging.basicConfig(level=logging.INFO)

# +
# dag.render()
# dag['clean_title_basics'].build()
# -

dag.build()

tconst = pd.read_parquet(str(dag['clean_title_episode']))

ep[ep.parentTconst == 'tt0468569']

ep = pd.read_parquet(str(dag['raw_title_episode']))
ep

titles = pd.read_parquet(str(dag['clean_title_basics']))

# +
# titles.groupby('tconst').size()
# -

tprincipals = pd.read_parquet(str(dag['raw_title_principals']))

tprincipals.shape

titles.head()

tprincipals = tprincipals.merge(titles[['tconst']], on='tconst', how='inner')
tprincipals.shape

tprincipals.head()

# 'director' 'actor', 'actress'
tprincipals = tprincipals[tprincipals.category.isin(['director'])]
# tprincipals = tprincipals[tprincipals.ordering <= 5]
tprincipals.shape

tprincipals[tprincipals.nconst == 'nm0000235']

nbasics = pd.read_parquet(str(dag['raw_name_basics'].product))

# +
# tbasics = pd.read_parquet(str(dag['raw_title_basics'].product))

# +
# tbasics.titleType.unique()

# +
# tbasics[tbasics.primaryTitle == 'The Dark Knight']

# +
# a = tprincipals[tprincipals.nconst == 'nm0000235']
# a.merge(titles, on='tconst')

# +
appearances = tprincipals.groupby('nconst').size()

appearances.sort_values(ascending=False, inplace=True)

appearances = pd.DataFrame({'nconst': appearances})

appearances.columns = ['size']
appearances.head()

# +
# nbasics[nbasics.primaryName == 'Uma Thurman']

# +
# William Beaudine
# https://www.imdb.com/name/nm0064415/?ref_=fn_al_nm_1

# +
# stratify by decade?
# mention that if we take the top director we are ignoring
# the temporal dimension, we cannot apply this to future data
# better to build this feature: #of movies by this director
# up to the release date
appearances = appearances.merge(nbasics, on='nconst')

appearances.head(100)

# -

appearances[appearances.primaryName == 'Uma Thurman']

name = pd.read_parquet(str(dag['raw_name_basics']))
name.shape

df = pd.read_parquet(str(dag['feats']))
df.head()

df.shape

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

clf = RandomForestRegressor(n_estimators=50, n_jobs=-1)

X = df.drop('averageRating', axis='columns')
y = df.averageRating

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# +
import numpy as np

(y_pred - y_test).abs().mean()
# -

y_test.mean(), y_test.min(), y_test.max()

imps = [(ft, imp) for ft, imp in zip(X_train.columns, clf.feature_importances_)]

sorted(imps, key=lambda x:x[1])

# +
import shap

shap.initjs()
# -

explainer = shap.TreeExplainer(clf)

shap_values = explainer.shap_values(X_train)

shap.force_plot(explainer.expected_value, shap_values[0,:], X_train.iloc[0,:])
