from basic_pipeline import pipeline


def test_pipeline_runs():
    dag = pipeline.make()

    dag.build()
