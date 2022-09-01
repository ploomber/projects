import os
from project_folder_handler import project_folder_handler

directory = '../../'

for dir_path, dir_names, file_names in os.walk(directory):
    if dir_path.startswith(directory + 'venv'):
        continue
    if 'pipeline.yaml' in file_names:
        project_folder_handler(dir_path)
