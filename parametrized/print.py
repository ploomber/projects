from pathlib import Path

# + tags=["parameters"]
upstream = None
product = None
some_param = None

# +
Path(product).parent.mkdir(parents=True, exist_ok=True)

# +
print('some_param: ', some_param, ' type: ', type(some_param))
