# %%
import yaml
import click

# %%
from ploomberutils.argo import is_valid_name


# %%
@click.group()
def cli():
    pass


# %%
@cli.command()
@click.argument('path')
def validate_argo(path):
    with open(path) as f:
        d = yaml.safe_load(f)

    names = [t['name'] for t in d['spec']['templates'][-1]['dag']['tasks']]
    invalid = [n for n in names if not is_valid_name(n)]

    if invalid:
        raise ValueError(f'Invalid task names: {invalid!r}')


# %%
if __name__ == '__main__':
    cli()
