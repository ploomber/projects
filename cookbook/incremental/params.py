import json
from pathlib import Path


def get_index(path_to_index):
    path = Path(path_to_index)

    if not path.exists():
        return -1

    index = json.loads(path.read_text())
    return index['latest']
