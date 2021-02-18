from ploomber.executors import Serial
from ploomber.spec import DAGSpec


def test_train():
    """
    This is a smoke test. It only check that the training pipeline runs
    (doesn't check if the output is correct). It passes a sample of the data
    to make it faster.
    """
    # load dag
    dag = DAGSpec.find(env={
        'products': '{{root}}/testing',
        'sample': True
    }).to_dag()

    # change executor settings: you can use "pytest --pdb" to start a debugging
    # session if the test fails. Calling dag['task'].debug() is another
    # option
    dag.executor = Serial(build_in_subprocess=False, catch_exceptions=False)

    # a third approach for debugging is to use: import IPython; IPython.embed()
    # to start an interactive session at this point. To do so, you must call
    # "pytest -s"

    dag.build()
