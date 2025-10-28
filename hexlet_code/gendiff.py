from .parser import parse_file
from .diff_builder import build_diff
from .formatters.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)

    raise ValueError(f"Unknown format: {format_name}")
