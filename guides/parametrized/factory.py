from ploomber import DAG


def make(param: str, another: int = 10):
    dag = DAG()
    # add tasks to your pipeline...
    return dag
