import json
from random import randint


def variable():
    """
    A task that generates a variable number of products (keys are filenames,
    values are products)
    """
    return {f'{x}.txt': str(x) for x in range(randint(1, 5))}


def many_products_one_variable():
    """
    A task that generates a fixed-size product ('one') and a variable-size
    product ('variable')
    """
    return {
        'one': 1,
        'variable': {f'{x}.txt': str(x)
                     for x in range(randint(1, 5))}
    }


def variable_downstream(upstream):
    """
    A task that dumps to JSON the output of "variable"
    """
    return json.dumps(upstream['variable'])


def many_products_one_variable_downstream(upstream):
    """
    A task that dumps to JSON the output "variable" of
    "many_products_one_variable"
    """
    return json.dumps(upstream['many_products_one_variable']['variable'])