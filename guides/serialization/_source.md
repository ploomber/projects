---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


# Serialization

<!-- start description -->
Tutorial explaining how the serializer and unserializer fields in a pipeline.yaml file work.
<!-- end description -->

Incremental builds allow Ploomber to skip tasks whose source code hasn't changed; each task must save their products to disk to enable such a feature. However, there are some cases when we don't want our pipeline to perform disk operations. For example, if we're going to deploy our pipeline, eliminating disk operations reduces runtime considerably.

To enable a pipeline to work in both disk-based and in-memory scenarios, we can declare a `serializer` and `unzerializer` in our pipeline declaration, effectively separating our task's logic from the read/write logic.

Note that this only applies to function tasks; other tasks are unaffected by the `serializer`/`unserializer` configuration.


## Built-in pickle serialization

The easiest way to get started is to use the built-in serializer and unserializer, which use the `pickle` module.

Let's see an example; the following pipeline has two tasks. The first one generates a dictionary, and the second one creates two dictionaries. Since we are using the pickle-based serialization, each dictionary is saved in the pickle binary format:

<% expand('simple.yaml') %>

Let's take a look at the task's source code:

<% expand('tasks.py') %>

Since we configured a `serializer` and `unserializer`, function tasks must `return` their outpues instead of saving them to disk in the function's body.

`first` does not have any upstream dependencies and returns a dictionary. `second` has the previous task as dependency and returns two dictionaries. Note that the keys in the returned dictionary must match the names of the products declared in `pipeline.yaml` (`another`, `final`).

Let's now run the pipeline.

```sh
ploomber build --entry-point simple.yaml --force
```

The pickle format has important [security concerns](https://docs.python.org/3/library/pickle.html), **remember only to unpickle data you trust**.


## Custom serialization logic

We can also define our own serialization logic, by using the `@serializer`, and `@unserializer` decorators. Let's replicate what our pickle-based serializer/unserializer is doing as an example:

<% expand('custom.py', symbols=['my_pickle_serializer', 'my_pickle_unserializer']) %>

A `@serializer` function must take two arguments: the object to serializer and the product object (taken from the task declaration). The `@unserializer` must take a single argument (the product to unserializer), and return the unserializer object.

Let's modify our original pipeline to use this serializer/unserializer:

<% expand('custom.yaml') %>

```sh
ploomber build --entry-point custom.yaml --force
```

## Custom serialization logic based on the product's extension

Under many circumstances, there are more suitable formats than pickle. For example, we may want to store lists or dictionaries as JSON files and other files using pickle. The `@serializer`/`@unserializer` decorators use mapping as the first argument to dispatch to different functions depending on the product's extension. Let's see an example:

<% expand('custom.py', symbols=['write_json', 'read_json', 'my_serializer', 'my_unserializer']) %>

Let's modify our example pipeline. The product in the first task does not have an extension (`output/one_dict`), hence, it will use pickle-based logic. However, the tasks in the second task have a `.json` extension, and will be saved as JSON files.

<% expand('with-json.yaml') %>

```sh
ploomber build --entry-point with-json.yaml --force
```

Let's print the `.json` files to verify they're not pickle files:

```sh
cat output/another_dict.json
```


```sh
cat output/final_dict.json
```

## Using a fallback format

Since it's common to have a `fallback` serialization format, the decorators have a `fallback` argument that, when enabled, uses the `pickle` module when the product's extension does not match any of the registered ones in the first argument.

The example works the same as the previous one, except we don't have to write our pickle-based logic.

`fallback` can also take the [joblib](https://github.com/joblib/joblib) or [cloudpickle](https://github.com/cloudpipe/cloudpickle) values. They're similar to the pickle format but have some advantages. For example, `joblib` produces smaller files when the serialized object contains many NumPy arrays, while cloudpickle supports serialization of some objects that the pickle module doesn't. To use `fallback='joblib'` or `fallback='cloudpickle'` the corresponding module must be installed.

<% expand('custom.py', symbols=['my_fallback_serializer', 'my_fallback_unserializer']) %>

<% expand('fallback.yaml') %>

```sh
ploomber build --entry-point fallback.yaml --force
```

Let's print the JSON files to verify their contents:

```sh
cat output/another_dict.json
```

```sh
cat output/final_dict.json
```

## Using default serializers

Ploomber comes with a few convenient serialization functions to write more succint serializers. We can request the use of such default serializers using the `defaults` argument, which takes a list of extensions:

<% expand('custom.py', symbols=['my_defaults_serializer', 'my_defaults_unserializer']) %>

Here we're asking to dispatch `.json` products and use `pickle` for all other extensions, the same as we did for the previous examples, except this time, we don't have to pass the mapping argument to the decorators.

`defaults` support:

1. `.json`: the returned object must be JSON-serializable (e.g., a list or a dictionary)
2. `.txt`: the returned object must be a string
3. `.csv`: the returned object must be a `pandas.DataFrame`
4. `.parquet`: the returned object must be a `pandas.DataFrame,` and a parquet library should be installed (such as `pyarrow`).

<% expand('defaults.yaml') %>

```sh
ploomber build --entry-point defaults.yaml --force
```

Let's print the JSON files to verify their contents:

```sh
cat output/another_dict.json
```

```sh
cat output/final_dict.json
```

## Wrapping up

Configuring a `serializer` and `unserializer` in your `pipeline.yaml` is optional, but it helps you quickly generate a fully in-memory pipeline for serving predictions.

If you want to learn more about in-memory pipelines, check out the [following guide](https://docs.ploomber.io/en/latest/deployment/online.html).

For a complete example showing how to manage a training and a serving pipeline, and deploy it as a Flask API, [click here](https://github.com/ploomber/projects/tree/master/templates/ml-online).
