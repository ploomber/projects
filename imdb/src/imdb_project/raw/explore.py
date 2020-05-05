# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from imdb_project import pipeline

import pandas as pd
# -

dag = pipeline.make()


list(dag)

# ## Episodes
#
# Each tconst has a parentTconst, which is a link between a series and their episodes. We only care
# about series or movies (not single episodes) so we'll only use the parents.

tepisode = pd.read_parquet(str(dag['raw_title_episode']))
tepisode.head()

# There are some series with lots of episodes!

sizes = tepisode.groupby('parentTconst').size().sort_values(ascending=False)
dsizes.head()

# ## Names

nbasics = pd.read_parquet(str(dag['raw_name_basics'].product))

nbasics.head()

# ## Titles

tbasics = pd.read_parquet(str(dag['raw_title_basics'].product))
tbasics.head()

# So this is the show with the most episodes: https://en.wikipedia.org/wiki/Days_of_Our_Lives

tbasics[tbasics.tconst == sizes.index[0]]

tbasics.titleType.unique()

tbasics.isAdult.unique()

tbasics.startYear.isna().mean(), tbasics.endYear.isna().mean()

tbasics.runtimeMinutes.isna().mean()

tbasics[~tbasics.runtimeMinutes.isna()]

tokens = [t.split(',') for t in tbasics.genres.unique() if t is not None]

tokens = [item for sublist in tokens for item in sublist]

set(tokens)

# ## AKAs

takas = pd.read_parquet(str(dag['raw_title_akas'].product))
takas.head()

tcrew = pd.read_parquet(str(dag['raw_title_crew'].product))
tcrew.head()

# ## Principals

tprincials = pd.read_parquet(str(dag['raw_title_principals'].product))
tprincials.head()


# ## Rating

trating = pd.read_parquet(str(dag['raw_title_ratings'].product))
trating.head()


