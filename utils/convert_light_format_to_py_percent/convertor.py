import os
def convertor(file_path: str):
    os.system(f'jupytext {file_path} --to py:percent')