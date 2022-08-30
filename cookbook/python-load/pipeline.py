# %%
from ploomber.constants import TaskStatus
from ploomber.spec import DAGSpec
from ploomber import with_env


# %%
@with_env('env.yaml')
# NOTE: you may add extra arguments to the function, they'll show up in the cli
def make(env):
    """Simplest factory function

    Examples
    --------
    Execute in the terminal:
        ploomber build -e pipeline.make
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    # NOTE: a factory function must return a DAG (do not call any methods)
    return dag


# %%
@with_env('env.yaml')
def delete_tasks(env):
    """Factory function that deletes tasks based on an input parameter

    Examples
    --------
    Execute in the terminal:
        ploomber build -e pipeline.delete_tasks --env--delete_tasks true
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()

    if env.delete_tasks:
        del dag['create_another']
        del dag['create_final']

    return dag


# %%
@with_env('env.yaml')
def ignore_task_status(env):
    """Factory function that overwrites a task's status and skips it

    Examples
    --------
    Execute in the terminal:
        ploomber task create_file --force
        ploomber build -e pipeline.ignore_task_status --force
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    dag.render()

    # NOTE: this example uses private APIs, and they may not work in the
    # future. Keep an eye on: https://github.com/ploomber/ploomber/issues/681
    # for updates

    # never execute the "create_file" tasl
    dag['create_file']._exec_status = TaskStatus.Skipped
    # this is necessary to prevent ploomber from overwriting the status
    dag._params.cache_rendered_status = True
    return dag
