from pathlib import Path
import pickle
import json

from ploomber.io import serializer, unserializer


@serializer()
def my_pickle_serializer(obj, product):
    Path(product).write_bytes(pickle.dumps(obj))


@unserializer()
def my_pickle_unserializer(product):
    return pickle.loads(Path(product).read_bytes())


def write_json(obj, product):
    Path(product).write_text(json.dumps(obj))


def read_json(product):
    return json.loads(Path(product).read_text())


@serializer({'.json': write_json})
def my_serializer(obj, product):
    Path(product).write_bytes(pickle.dumps(obj))


@unserializer({'.json': read_json})
def my_unserializer(product):
    return pickle.loads(Path(product).read_bytes())


@serializer({'.json': write_json}, fallback=True)
def my_fallback_serializer(obj, product):
    pass


@unserializer({'.json': read_json}, fallback=True)
def my_fallback_unserializer(product):
    pass


@serializer(fallback=True, defaults=['.json'])
def my_defaults_serializer(obj, product):
    pass


@unserializer(fallback=True, defaults=['.json'])
def my_defaults_unserializer(product):
    pass
