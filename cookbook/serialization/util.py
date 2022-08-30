# %%
from ploomber.io import serializer, unserializer


# %%
@serializer(fallback='joblib', defaults=['.csv', '.txt'])
def my_serializer(obj, product):
    pass


# %%
@unserializer(fallback='joblib', defaults=['.csv', '.txt'])
def my_unserializer(product):
    pass
