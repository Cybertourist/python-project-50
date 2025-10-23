import json


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1:
        data1 = json.load(f1)
    with open(file_path2) as f2:
        data2 = json.load(f2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = ['{']

    for key in keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {to_str(data1[key])}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {to_str(data2[key])}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {to_str(data1[key])}")
        else:
            diff_lines.append(f"  - {key}: {to_str(data1[key])}")
            diff_lines.append(f"  + {key}: {to_str(data2[key])}")

    diff_lines.append('}')
    return '\n'.join(diff_lines)
