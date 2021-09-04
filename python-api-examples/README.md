# Python API examples

This folder contains examples and tutorials using the Python API.

If you're looking for a complete project layout using the Python API, see the [python-api/](../python-api) directory.

## Guides

Guides explain Ploomber's concepts.

### Essential

* [Core concepts](guide/core.ipynb)
* [Managing pipeline configuration with Environment](guide/env.ipynb)
* [Task's parameters resolution](guide/param-resolution.ipynb)
* [Managing scripts (SQL, Python)](guide/static.ipynb)

### Intermediate

* [Work in progress] [Pipeline and task hooks](guide/hooks.ipynb)

### Advanced

* [Debugging pipelines](guide/debugging.ipynb)
* [Understanding the Environment life cycle](guide/env-life-cycle.ipynb)
* [Advanced pipeline coniguration](guide/dag-configurator.ipynb)

## Examples

Short examples that show Ploomber's features.

* [Basic pipeline](examples/basic.py)
* [Adding tasks dynamically](examples/dynamic.py)
* [Parametrized and re-usable SQL scripts](examples/loader.py)
* [Parametrizing tasks](examples/parametrizing.py)
* [Task grids](examples/param_grid.py)
* [Storing predictions in a database table](examples/polling.py)
* [Data quality testing](examples/testing.py)
* [Environments with the `@with_env` decorator](examples/with_env.py)
* [Factories: functions that return pipelines](examples/factories.py)
