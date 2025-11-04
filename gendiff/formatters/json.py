import json  #NOSONAR


def format_json(diff):  #NOSONAR
    """Возвращает diff в формате JSON."""
    return json.dumps(diff, indent=2)  #NOSONAR
