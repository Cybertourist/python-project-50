INDENT = 4


def format_value(value, depth):
    """Format primitive or nested dict value to stylish representation."""
    if isinstance(value, dict):
        lines = []
        inner_indent = " " * (depth * INDENT)
        for k, v in value.items():
            line = f"{inner_indent}    {k}: {format_value(v, depth + 1)}"
            lines.append(line)
        closing_indent = " " * (depth * INDENT)
        body = "\n".join(lines)
        return "{\n" + body + f"\n{closing_indent}}}"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=0):
    """Format diff tree into stylish string."""
    lines = []
    current_indent = " " * (depth * INDENT)

    for node in diff:
        key = node["key"]
        status = node["status"]

        if status == "nested":
            children_repr = format_stylish(node["children"], depth + 1)
            lines.append(f"{current_indent}    {key}: {children_repr}")
        elif status == "added":
            val = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  + {key}: {val}")
        elif status == "removed":
            val = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {val}")
        elif status == "unchanged":
            val = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}    {key}: {val}")
        elif status == "changed":
            old_v = format_value(node["old_value"], depth + 1)
            new_v = format_value(node["new_value"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {old_v}")
            lines.append(f"{current_indent}  + {key}: {new_v}")

    closing_indent = " " * (depth * INDENT)
    return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
