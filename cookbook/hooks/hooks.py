# %%
"""
DAG-level and task-level hooks. All arguments in the functions are optional
"""


# %%
def dag_level_on_render(my_param):
    """Executed after the pipeline renders (before execution)
    """
    print(f'rendered DAG! my_param={my_param}')


# %%
def dag_level_on_finish(dag, report):
    """Executes after the pipeline runs all tasks
    """
    print(f'Finished executing pipeline {dag}, report:\n{report}')


# %%
def dag_level_on_failure(traceback):
    """Executes if the pipeline fails
    """
    if traceback.get('build'):
        print('Pipeline execution failed while running the tasks!')

    if traceback.get('on_finish'):
        print('Pipeline execution failed while executing an on_finish hook!')


# %%
def on_render(my_param, task, client, product, params):
    """Executed after the task renders (before execution)
    """
    print(f'Finished rendering {task.name} with my_param {my_param}, '
          f'client {client}, product {product}, and task params {params}')


# %%
def on_finish(task, client, product, params):
    """Executes after the task runs
    """
    print(f'Finished running {task.name} with client {client}, '
          f'product {product} and params {params}')


# %%
def on_failure(task, client, product, params):
    """Executes if the task fails
    """
    print(f'{task.name} with client {client}, '
          f'product {product} and params {params} failed!')
