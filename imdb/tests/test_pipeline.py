from imdb_project import pipeline


def test_build_dag():
    dag = pipeline.make()
    dag.build()
