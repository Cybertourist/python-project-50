def format_value(value, depth):
    """Форматирует значение (включая вложенные словари) с правильными отступами."""
    if isinstance(value, dict):
        indent_size = depth * 4
        current_indent = ' ' * indent_size
        lines = []
        for k, v in value.items():
            lines.append(f"{current_indent}    {k}: {format_value(v, depth + 1)}")
        closing_indent = ' ' * indent_size
        return f"{{\n{'\n'.join(lines)}\n{closing_indent}}}"
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=0):
    """Рекурсивно форматирует diff-дерево в виде 'stylish'."""
    indent_size = depth * 4
    current_indent = ' ' * indent_size
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}    {key}: {children}")
        elif node_type == 'added':
            lines.append(f"{current_indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif node_type == 'removed':
            lines.append(f"{current_indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif node_type == 'unchanged':
            lines.append(f"{current_indent}    {key}: {format_value(node['value'], depth + 1)}")
        elif node_type == 'changed':
            lines.append(f"{current_indent}  - {key}: {format_value(node['old_value'], depth + 1)}")
            lines.append(f"{current_indent}  + {key}: {format_value(node['new_value'], depth + 1)}")

    closing_indent = ' ' * (indent_size)
    return f"{{\n{'\n'.join(lines)}\n{closing_indent}}}"
