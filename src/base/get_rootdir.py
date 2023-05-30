from pathlib import Path


def root_path():
    return str(Path(__file__).parent.parent.parent)
