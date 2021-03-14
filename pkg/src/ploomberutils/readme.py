from importlib import resources

import ploomberutils
from jinja2 import Template


def render():
    # pandas is an optional dependency, no needed for CI
    import pandas as pd

    template = Template(
        resources.read_text(ploomberutils, 'README-template.md'))

    df = pd.read_csv('index.csv', encoding='utf-8')
    df.index = df.index + 1

    basic = df[df.type == 'basic'].drop('type', axis='columns')
    intermediate = df[df.type == 'intermediate'].drop('type', axis='columns')
    advanced = df[df.type == 'advanced'].drop('type', axis='columns')

    return template.render(basic=basic.to_records(),
                           intermediate=intermediate.to_records(),
                           advanced=advanced.to_records())
