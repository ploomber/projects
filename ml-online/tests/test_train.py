from ploomber.spec import DAGSpec


def test_train():
    """
    This is a smoke test. It only check that the training pipeline runs
    (doesn't check if the output is correct). It passes a sample of the data
    to make it faster.
    """
    # DAGSpec.find automatically finds your pipeline.yaml
    dag = DAGSpec.find(env={
        'products': '{{root}}/testing',
        'sample': True
    }).to_dag()

    # same as calling "ploomber build --force"
    dag.build(force=True)
