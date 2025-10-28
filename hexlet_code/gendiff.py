from .parser import parse_file


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = ['{']

    for key in keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {data1[key]}")
        else:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")

    diff_lines.append('}')
    return '\n'.join(diff_lines)
