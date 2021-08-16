def first():
    return dict(a=1, b=2)


def second(upstream):
    first = upstream['first']
    another = dict(a=first['b'] + 1, b=first['a'] + 1)
    final = dict(a=100, b=200)
    return dict(another=another, final=final)
