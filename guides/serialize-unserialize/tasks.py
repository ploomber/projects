def first():
    return dict(a=1, b=2)


def second(upstream):
    another = dict(a=upstream['first']['b'] + 1, b=upstream['first']['a'] + 1)
    final = dict(a=100, b=200)
    return dict(another=another, final=final)
