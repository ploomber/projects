import re


def is_valid_name(name):
    return re.match(r'^[a-zA-Z0-9]{1}[a-zA-Z0-9\-]+$', name) is not None
