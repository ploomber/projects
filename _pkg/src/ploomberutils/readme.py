from pathlib import Path

import jupytext
from jinja2 import Template
import papermill as pm
from ploomber.tasks import PythonCallable
from ploomber.products import File


def _render(resources_, product):
    """
    Generate README.md from _source.md
    """

    # pandas is an optional dependency, no needed for CI
    import pandas as pd

    template = Template(Path(resources_['source']).read_text())

    df = pd.read_csv('index.csv', encoding='utf-8')
    df.index = df.index + 1

    basic = df[df.type == 'basic'].drop('type', axis='columns')
    intermediate = df[df.type == 'intermediate'].drop('type', axis='columns')
    advanced = df[df.type == 'advanced'].drop('type', axis='columns')

    out = template.render(basic=basic.to_records(),
                          intermediate=intermediate.to_records(),
                          advanced=advanced.to_records())

    Path(product).write_text(out)


def render(dag):
    return PythonCallable(_render,
                          File('README.md'),
                          dag=dag,
                          params=dict(resources_=dict(source='_source.md')))


def _execute(upstream, product):
    """
    Generate README.ipynb from _source.md
    """
    nb = jupytext.read(str(upstream.first))
    jupytext.write(nb, str(product))
    pm.execute_notebook(str(product), str(product), kernel_name='python3')


def execute(dag):
    return PythonCallable(_execute, File('README.ipynb'), dag=dag)
