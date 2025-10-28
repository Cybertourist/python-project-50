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
            lines.append(format_plain(node['children'], f"{property_path}."))
        elif status == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{property_path}' was added with value: "
                f"{value}"  # Первая часть
            )
        elif status == 'removed':
            lines.append(
                f"Property '{property_path}' was removed"
            )
        elif status == 'changed':
            old = format_value(node['old_value'])
            new = format_value(node['new_value'])

            # Разделим строку явно на несколько частей
            lines.append(
                f"Property '{property_path}' was updated. "  # Первая часть
                f"From {old} "  # Вторая часть
                f"to {new}"  # Третья часть
            )

    return '\n'.join(filter(None, lines))
