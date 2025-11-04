import json


def format_json(diff):
    """Возвращает diff в формате JSON."""
    return json.dumps(diff, indent=2)
