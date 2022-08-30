# %%
import json
from pathlib import Path

# %%
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

# %%
default_args = {
    'start_date': days_ago(0),
}

# %%
dag = DAG(
    dag_id='content',
    default_args=default_args,
    description='Ploomber DAG (content)',
    schedule_interval=None,
)

# %%
path_to_spec = Path(__file__).parent / 'content.json'
spec = json.loads(path_to_spec.read_text())

# %%
for task in spec['tasks']:
    BashOperator(
        bash_command=task['command'],
        task_id=task['name'],
        dag=dag,
        cwd="/content"
    )

# %%
for task in spec['tasks']:
    t = dag.get_task(task['name'])

    for upstream in task['upstream']:
        t.set_upstream(dag.get_task(upstream))
