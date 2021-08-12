from collections.abc import Mapping
from pathlib import Path

import pandas as pd
import joblib


def serializer(obj, product):
    """
    Serializes products. Handles tasks that return a single or multiple
    products (a dictionary)
    """
    # task has multiple products...
    if isinstance(product, Mapping):
        for key, product in product.to_json_serializable().items():
            _serialize_dispatch(obj[key], product)
    # single product...
    else:
        _serialize_dispatch(obj, product)


def unserializer(product):
    """
    Unserializes products. Handles tasks that return a single or multiple
    products (a dictionary)
    """
    # task has multiple products...
    if isinstance(product, Mapping):
        return {
            key: _unserialize_dispatch(obj)
            for key, obj in product.to_json_serializable().items()
        }
    # single product...
    else:
        return _unserialize_dispatch(product)


def _serialize_dispatch(obj, product):
    """Determines which serializer function to use depending on the extension
    """
    product_path = Path(product)
    product_path.parent.mkdir(parents=True, exist_ok=True)

    serializers_by_suffix = {
        '.txt': _serialize_txt,
        '.csv': _serialize_csv,
        '.joblib': _serialize_joblib,
    }

    try:
        serializer = serializers_by_suffix[product_path.suffix]
    except KeyError as e:
        raise ValueError('No serializer registered for products '
                         f'with suffix: {product_path.suffix!r}') from e

    return serializer(obj, product_path)


def _unserialize_dispatch(product):
    """Determines which unserializer function to use depending on the extension
    """
    product_path = Path(product)

    unserializers_by_suffix = {
        '.txt': _unserialize_txt,
        '.csv': _unserialize_csv,
        '.joblib': _unserialize_joblib,
    }

    try:
        unserializer = unserializers_by_suffix[product_path.suffix]
    except KeyError as e:
        raise ValueError('No unserializer registered for products '
                         f'with suffix: {product_path.suffix!r}') from e

    return unserializer(product_path)


def _serialize_csv(obj, product):
    obj.to_csv(product)


def _serialize_txt(obj, product):
    Path(product).write_text(obj)


def _serialize_joblib(obj, product):
    joblib.dump(obj, str(product))


def _unserialize_csv(product):
    return pd.read_csv(product)


def _unserialize_txt(product):
    return Path(product).read_text()


def _unserialize_joblib(product):
    return joblib.load(product)
