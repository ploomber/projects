import os
import zipfile
import subprocess


def test_wheel_includes_pipeline_and_model(tmp_path):
    subprocess.run([
        'python',
        'setup.py',
        'bdist_wheel',
        '--dist-dir',
        str(tmp_path),
    ])

    name = os.listdir(tmp_path)[0]

    with zipfile.ZipFile(tmp_path / name, 'r') as zip_ref:
        zip_ref.extractall(tmp_path)

    names = [
        'pipeline.yaml',
        'pipeline-features.yaml',
        'model.pickle',
        'env.yaml',
    ]

    assert all([(tmp_path / 'ml_online' / name).exists() for name in names])
