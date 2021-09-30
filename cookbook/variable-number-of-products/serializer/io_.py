from ploomber.io import serializer, unserializer


@serializer(fallback='joblib', defaults=['.json', '.txt'], unpack=True)
def my_serializer(obj, product):
    pass


@unserializer(fallback='joblib', defaults=['.json', '.txt'], unpack=True)
def my_unserializer(product):
    pass
