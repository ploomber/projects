from imdb_project import pipeline

dag = pipeline.make()

dag.build()

dag.plot()
