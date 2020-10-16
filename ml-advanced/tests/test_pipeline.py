import pytest
from ploomber import Env
from ploomber.executors import Serial

from ml_advanced import pipeline


@pytest.fixture()
def test_env():
    env = Env('env.test.yaml')
    yield env
    env.end()


def test_pipeline(test_env, force):
    # test is executed with a sample of the data
    dag = pipeline._make(test_env)

    # customize executor for testing purposes, default settings will not
    # start the debugger in the line that raised the exception, this
    # settings will, try adding an exception in any of the PythonCallable
    # tasks then run pytest --pdb to see it in action
    dag.executor = Serial(build_in_subprocess=False, catch_exceptions=False)

    dag.build(force=force)
