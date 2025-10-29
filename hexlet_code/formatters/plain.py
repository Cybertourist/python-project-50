def format_value(value):
    """Форматирует значение для plain-вывода."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def format_plain(diff, path=''):
    """Рекурсивно форматирует diff-структуру в plain-текст."""
    lines = []

    for node in diff:
        key = node['key']
        status = node['status']
        property_path = f"{path}{key}"

        if status == 'nested':
            # Рекурсивно спускаемся в children
            lines.append(format_plain(node['children'], f"{property_path}."))
        elif status == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )
        elif status == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif status == 'changed':
            old = format_value(node['old_value'])
            new = format_value(node['new_value'])
            lines.append(
                f"Property '{property_path}' was updated. From {old} to {new}"
            )
        elif status == 'unchanged':
            # Пропускаем — в plain-формате не показываем неизменённые
            continue

    return '\n'.join(lines)

