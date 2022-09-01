from typing import List
from convertor import convertor
import yaml

def project_folder_handler(dir_path: str):
    pipeline_file = dir_path + '/pipeline.yaml'
    with open(pipeline_file, 'r') as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
        if 'tasks' not in data:
            return
        tasks: List[dict] = data['tasks']
        for task in tasks:
            if 'source' not in task:
                continue
            script_file: str = task['source']
            if not script_file.endswith('.py'):
                continue

            script_file_path = dir_path + '/' + script_file
            convertor(script_file_path)
