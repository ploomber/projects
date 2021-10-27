from ploomber.spec import DAGSpec
from ploomber import with_env


@with_env('env.yaml')
# NOTE: you may add other params to the function, they'll show up in the cli
def make(env):
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    # NOTE: return the DAG, do not call any methods
    return dag
