# %%
import pandas as pd
from ploomber.testing.sql import nulls_in_columns, range_in_column


# %%
def test_sql_clean(client, product):
    """Tests for clean.sql
    """
    assert not nulls_in_columns(client, ['score', 'age'], product)
    min_age, max_age = range_in_column(client, 'age', product)
    assert min_age > 0


# %%
def test_py_transform(product):
    """Tests for transform.py
    """
    df = pd.read_csv(str(product['data']))
    assert not df.multiplied_score.isna().sum()
    assert df.multiplied_score.min() >= 0
