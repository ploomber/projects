"""
Tasks to get raw data
"""

import csv
import pandas as pd


def get_data_from_url(product, url):
    """Download TSV file from a URL

    Notes
    -----
    * title.basics dataset has a line like this:
        [TAB]"Rolling in the Deep Dish[TAB]"Rolling in the Deep Dish
        so we need to disable quoting to avoid errors
    * na_value is documented in the data description
    """
    df = pd.read_csv(url, sep='\t', quoting=csv.QUOTE_NONE, na_values='\\N')
    df.to_parquet(str(product))
