# Serialization

Incremental builds allows Ploomber to skip tasks whose source code hasn't changed; to enable such a feature, each task must save their products to disk. However, there are some cases when we don't want our pipeline to perform disk operations. For example, if we want to deploy our pipeline, eliminating disk operations reduces runtime considerably.

To enable a pipeline to work in both disk-based and in-memory scenarios, we can declare a `serializer` and `unzerializer` in our pipeline declaration, effectively separating our task's logic from the read/write logic.

Note that this only applies to function tasks, other tasks are unaffected by the `serializer`/`unserializer` configuration.

```python
from ploomberutils import display_file
```

## Built-in pickle serialization

The easiest way to get started is to use the built-in serializer and unserializer which use the `pickle` module.

Let's see an example, the following pipeline has two tasks, the first one generates a dictionary and the second one two dictionaries. Since we are using the pickle-based serialization, each dictionary is saved in the pickle binary format:

```python
display_file('simple.yaml')
```

```sh
ploomber build --entry-point simple.yaml --force
```

The pickle format has important [security concerns](https://docs.python.org/3/library/pickle.html), **remember to only unpickle data you trust**.


## Custom serialization logic

We can also define our own serialization logic, by using the `@serializer`, and `@unserializer` decorators. Let's replicate what our pickle-based serializer/unserializer is doing as an example:

```python
display_file('custom.py', symbols=['my_pickle_serializer', 'my_pickle_unserializer'])
```

A `@serializer` function must take two arguments: the object to serializer and the product object (taken from the task declaration). The `@unserializer` must take a single argument (the product to unserializer), and return the unserializer object.

Let's modify our original pipeline to use this serializer/unserializer:

```python
display_file('custom.yaml')
```

```sh
ploomber build --entry-point custom.yaml --force
```

## Custom serialization logic based on the product's extension

Under many circumstances, there are more suitable formats than pickle. For example, we may want to store lists or dicts as JSON files, and any other files using pickle. The `@serializer`/`@unserializer` decorators take a mapping as first argument to dispatch to different functions depending on the product's extension. Let's see an example:

```python
display_file('custom.py', symbols=['write_json', 'read_json', 'my_serializer', 'my_unserializer'])
```

Let's modify our example pipeline. The product in the first task does not have an extension (`output/one_dict`), hence, it will use the pickle-based logic. However, the tasks in the second task have a `.json` extension, hence, they will be saved as JSON files.

```python
display_file('with-json.yaml')
```

```sh
ploomber build --entry-point with-json.yaml --force
```

Let's print the `.json` files to verify they're not pickle files:

```python
display_file('output/another_dict.json')
```

```python
display_file('output/final_dict.json')
```

## Using a fallback format

Since it's common to have a `fallback` serialization format. The decorators have a `fallback` argument that when enabled, uses the `pickle` module when the product's extension does not match any of the registered one in the first argument.

The example works the same as the previous one, except we don't have to write our own pickle-based logic.

`fallback` can also take the [joblib](https://github.com/joblib/joblib) or [cloudpickle](https://github.com/cloudpipe/cloudpickle) values. They're similar to the pickle format but have some advantages. For example, `joblib` produces smaller files when the serialized object contains many NumPy arrays, while cloudpickle supports serialization of some objects that the pickle module doesn't. To use `fallback='joblib'` or `fallback='cloudpickle'` the corresponding module must be installed.

```python
display_file('custom.py', symbols=['my_fallback_serializer', 'my_fallback_unserializer'])
```

```python
display_file('fallback.yaml')
```

```sh
ploomber build --entry-point fallback.yaml --force
```

Let's print the JSON files to verify their contents:

```python
display_file('output/another_dict.json')
```

```python
display_file('output/final_dict.json')
```

## Using default serializers

Ploomber comes with a few convenient serialization functions to write more succint serializers. We can request the use of such default serializers using the `defaults` argument, which takes a list of extensions:

```python
display_file('custom.py', symbols=['my_defaults_serializer', 'my_defaults_unserializer'])
```

Here we're asking to dispatch `.json` products and use `pickle` for all other extensions, the same as we did for the previous examples, except this time we don't have to pass the mapping argument to the decorators.

`defaults` supports:

1. `.json`: the returned object must be JSON-serializable (e.g., a list or a dictionary)
2. `.txt`: the returned object must be a string
3. `.csv`: the returned object must be a `pandas.DataFrame`
4. `.parquet`: the returned object must be a `pandas.DataFrame` and there should be a parquet library installed (such as `pyarrow`).

```python
display_file('defaults.yaml')
```

```sh
ploomber build --entry-point defaults.yaml --force
```

Let's print the JSON files to verify their contents:

```python
display_file('output/another_dict.json')
```

```python
display_file('output/final_dict.json')
```
