from .parser import parse_file
from .diff_builder import build_diff
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.formatters.plain import format_plain
from hexlet_code.formatters.json import format_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    if format_name == 'json':
        return format_json(diff)

    raise ValueError(f"Unknown format: {format_name}")
