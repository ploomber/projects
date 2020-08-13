def inner(x):
    if x == 42:
        raise ValueError


def middle(x):
    return inner(x)


def outer(x):
    return middle(x)
