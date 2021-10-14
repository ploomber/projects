from dataclasses import dataclass
from pathlib import Path
from glob import glob

import jupytext
from jinja2 import Template
import papermill as pm
from ploomber.tasks import PythonCallable
from ploomber.products import File
from jupyblog import md


@dataclass
class Example:
    path: str
    idx: int

    @property
    def description(self):
        content = Path(self.path, '_source.md').read_text()
        try:
            return md.extract_between_line_content(
                content, ('<!-- start description -->',
                          '<!-- end description -->')).strip()
        except Exception as e:
            raise ValueError(
                f'Could not extract description from {self.path}') from e

    @property
    def category(self):
        return str(Path(self.path).parent)

    def to_csv(self):
        elements = [self.idx, self.category, self.path, self.description]
        return ','.join(f'"{e}"' for e in elements)


def _render(resources_, product):
    """
    Generate README.md from _source.md
    """
    templates = [
        Example(path=path, idx=idx)
        for idx, path in enumerate(sorted(glob('templates/*')), start=1)
    ]

    cookbook = [
        Example(path=path, idx=idx)
        for idx, path in enumerate(sorted(glob('cookbook/*')), start=1)
    ]
    guides = [
        Example(path=path, idx=idx)
        for idx, path in enumerate(sorted(glob('guides/*')), start=1)
    ]

    template = Template(Path(resources_['source']).read_text())
    out = template.render(cookbook=cookbook,
                          guides=guides,
                          templates=templates)
    Path(product['readme']).write_text(out)

    lines = ['"idx","category","name","description"']

    for section in [templates, cookbook, guides]:
        for example in section:
            lines.append(example.to_csv())

    Path(product['index']).write_text('\n'.join(lines))


def render(dag):
    return PythonCallable(_render, {
        'readme': File('README.md'),
        'index': File('_index.csv')
    },
                          dag=dag,
                          params=dict(resources_=dict(source='_source.md')))


def _execute(upstream, product):
    """
    Generate README.ipynb from _source.md
    """
    nb = jupytext.read(str(upstream.first['readme']))
    jupytext.write(nb, str(product))
    pm.execute_notebook(str(product), str(product), kernel_name='python3')


def execute(dag):
    return PythonCallable(_execute, File('README.ipynb'), dag=dag)
