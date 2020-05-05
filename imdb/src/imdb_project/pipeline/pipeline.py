"""
Pipeline declaration
"""
from pathlib import Path
from functools import reduce
from pkg_resources import resource_filename

# tasks are grouped in separate modules
from imdb_project import raw as raw_module
from imdb_project import clean as clean_module
from imdb_project import features as features_module

from ploomber import load_env, with_env
from ploomber import DAG
from ploomber.tasks import TaskFactory, PythonCallable, NotebookRunner
from ploomber.products import File

@load_env
def make_get_raw_task(env, name, dag, url):
    """Create a task to download a raw dataset
    """
    return PythonCallable(raw_module.get_data_from_url,
                          product=File(env.path.raw /
                                       f'raw_{name}.parquet'),
                          dag=dag,
                          params=dict(url=url),
                          name=f'raw_{name}')

@with_env
def make(env):
    """Assemble the pipeline and return a DAG object
    """
    dag = DAG('imdb-pipeline')

    env.path.raw.mkdir(exist_ok=True, parents=True)

    for name in ['clean', 'features']:
        (env.path.processed / name).mkdir(exist_ok=True, parents=True)

    # task factory is a conveniend method to reduce boilerplate code
    # if many of our tasks have the same Task type and Product type,
    # this pipeline has only PythonCallable with File products so it's
    # a good use case
    factory = TaskFactory(PythonCallable, File, dag)

    # dictionaries for holding our tasks, we will use this to ease pipeline
    # assembly
    raw, clean, features = {}, {}, {}

    # for every url declared in env.yaml, create a task to download the dataset
    for name, url in env.raw_data_urls.items():
        raw[name] = make_get_raw_task(name, dag, url)

    # all raw dataset has a corresponding clean dataset, this loop creates
    # all clean dataset tasks
    for name, task_raw in raw.items():
        # to avoid boilerplate code, we are reusing the same names all
        # throughout the pipeline, so we can just get the function we need
        # with this line
        fn = getattr(clean_module, name)

        # the product will be stored in the [processed] / clean folder
        product_arg = env.path.processed / 'clean' / f'clean_{name}.parquet'

        # create the task
        task_clean = factory.make(fn, product_arg, name=f'clean_{name}')

        # the cleaning task depends on the raw task with the same name
        task_raw >> task_clean

        # store the clean task, we need it for the feature step
        clean[name] = task_clean

    clean['title_episode'] >> clean['title_basics']

    # pass all raw tasks to the explore notebook
    # raw_explore = NotebookRunner(Path(resource_filename('imdb_project',
    #                                                     'raw/explore.py')),
    #                              product=File(env.path.raw / 'explore.ipynb'),
    #                              dag=dag,
    #                              name='raw_explore')
    # raw_all = reduce(lambda x, y: x + y, raw.values())
    # raw_all >> raw_explore

    # this loop is very similar to the previous one, but for feature tasks
    for name, task_clean in clean.items():
        fn = getattr(features_module, name)
        product_arg = env.path.processed / 'features' / f'feat_{name}.parquet'
        task_features = factory.make(fn, product_arg, name=f'feat_{name}')
        task_clean >> task_features
        features[name] = task_features

    # after features are created, we need to join them in a single file
    # this tasks does that
    task_join = factory.make(features_module.join,
                             env.path.processed / 'features' / 'join.parquet',
                             name='feats')

    # create a task group by adding feature tasks together via t1 + t2 + ...
    features_all = reduce(lambda x, y: x + y, features.values())

    # join task depends on all feature tasks
    features_all >> task_join

    return dag


if __name__ == '__main__':
    dag = make()
    dag.plot()
