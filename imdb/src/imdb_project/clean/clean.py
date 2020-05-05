"""
Tasks to clean raw data
"""

import pandas as pd


def name_basics(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_basics(product, upstream):
    # TODO: test each title should appear at most once
    # TODO: add some logging
    # TODO: add note on one-hot-encoding (fit on training data, and only apply
    # on test)
    df = pd.read_parquet(str(upstream['raw_title_basics']))

    # only keep types we care about
    df = df[df.titleType.isin(['movie', 'tvMovie', 'tvSeries',
                               'tvMiniSeries'])]

    # only get movies or shows, do not use single episodes
    # episodes = pd.read_parquet(str(upstream['clean_title_episode']))
    # df = df.merge(episodes, on='tconst', how='inner')

    # df.drop(['endYear', 'runtimeMinutes'], axis='columns', inplace=True)

    df = df[~(df.genres.isna() | df.startYear.isna() |
              df.primaryTitle.isna() | df.originalTitle.isna())]

    # TODO: move to featurize
    tokens = [t.split(',') for t in df.genres.unique() if t is not None]
    genres = set([item for sublist in tokens for item in sublist])

    for genre in genres:
        df['genre_'+genre] = df.genres.str.contains(genre)

    df.drop('genres', axis='columns', inplace=True)

    df = pd.concat([df, pd.get_dummies(df.titleType)], axis=1)
    # df.drop(['titleType', 'primaryTitle', 'originalTitle'],
            # axis='columns', inplace=True)

    df.to_parquet(str(product))


def title_akas(product, upstream):
    # need this to convert from name id to actual name
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_crew(product, upstream):
    # NOTE: we might not need this...
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_episode(product, upstream):
    """
    Raw title_episode is a mapping between episodes -> show name, we only care
    about shows or movies, so we build the unique list of IDs here

    Notes
    -----
    This only applies for TV series and not for movies
    """
    df = pd.read_parquet(str(upstream.first))
    # only get movies or shows, remove single episodes
    parents = pd.DataFrame({'tconst': df.parentTconst.unique()})
    parents.to_parquet(str(product))


def title_principals(product, upstream):
    # TODO: use this to build features for director/actors
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_ratings(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))
