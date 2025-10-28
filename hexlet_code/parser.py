import json
import yaml
import os


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1]

    with open(filepath) as f:
        if ext in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        elif ext == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
