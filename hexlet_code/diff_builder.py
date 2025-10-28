def build_diff(data1, data2):
    """Строит внутреннее представление различий между двумя структурами."""
    diff = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Если ключ есть в обеих структурах и оба значения — словари, то идем вглубь
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(value1, value2)
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': value2
            })
        elif key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': value1
            })
        elif value1 != value2:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': value1,
                'new_value': value2
            })
        else:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': value1
            })

    return diff
