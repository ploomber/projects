"""
Tasks to generate features from clean datasets
"""
import logging

import pandas as pd


def name_basics(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_basics(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_akas(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_crew(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_episode(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_principals(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def title_ratings(product, upstream):
    df = pd.read_parquet(str(upstream.first))
    df.to_parquet(str(product))


def join(product, upstream):
    logger = logging.getLogger(__name__)
    logger.info('logging...')

    title = pd.read_parquet(str(upstream['feat_title_basics']))
    ratings = pd.read_parquet(str(upstream['feat_title_ratings']))
    df = title.merge(ratings, on='tconst', how='inner')
    df.drop('tconst', axis='columns', inplace=True)
    df.to_parquet(str(product))
