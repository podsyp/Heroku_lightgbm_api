from pathlib import Path

def get_version():
    p = Path(__file__).parents[1]

    with open(p / 'VERSION', 'r') as version_file:
        version = version_file.read().strip()

    return version
