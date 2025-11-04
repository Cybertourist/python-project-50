def format_value(value):  #NOSONAR
    """Форматирует значение для plain-вывода."""
    if isinstance(value, dict):  #NOSONAR
        return '[complex value]'  #NOSONAR
    if isinstance(value, str):  #NOSONAR
        return f"'{value}'"  #NOSONAR
    if value is True:  #NOSONAR
        return 'true'  #NOSONAR
    if value is False:  #NOSONAR
        return 'false'  #NOSONAR
    if value is None:  #NOSONAR
        return 'null'  #NOSONAR
    return str(value)  #NOSONAR


def format_plain(diff, path=''):  #NOSONAR
    """Рекурсивно форматирует diff-структуру в plain-текст."""
    lines = []  #NOSONAR

    for node in diff:  #NOSONAR
        key = node['key']  #NOSONAR
        status = node['status']  #NOSONAR
        property_path = f"{path}{key}"  #NOSONAR

        if status == 'nested':  #NOSONAR
            # Рекурсивно спускаемся в children
            lines.append(format_plain(node['children'], f"{property_path}."))  #NOSONAR
        elif status == 'added':  #NOSONAR
            value = format_value(node['value'])  #NOSONAR
            lines.append(  #NOSONAR
                f"Property '{property_path}' was added with value: {value}"  #NOSONAR
            )  #NOSONAR
        elif status == 'removed':  #NOSONAR
            lines.append(f"Property '{property_path}' was removed")  #NOSONAR
        elif status == 'changed':  #NOSONAR
            old = format_value(node['old_value'])  #NOSONAR
            new = format_value(node['new_value'])  #NOSONAR
            lines.append(  #NOSONAR
                f"Property '{property_path}' was updated. From {old} to {new}"  #NOSONAR
            )  #NOSONAR
        elif status == 'unchanged':  #NOSONAR
            # Пропускаем — в plain-формате не показываем неизменённые
            continue  #NOSONAR

    return '\n'.join(lines)  #NOSONAR
