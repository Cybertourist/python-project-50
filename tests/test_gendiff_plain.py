import os
import difflib
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def test_generate_diff_plain():
    """Тестирует вывод в plain-формате."""
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected = get_fixture_path('expected_plain.txt')

    with open(expected) as f:
        expected_output = f.read().strip()

    result = generate_diff(file1, file2, format_name='plain').strip()

    if result != expected_output:
        print("\n--- DIFF START ---")
        for line in difflib.unified_diff(
            expected_output.splitlines(),
            result.splitlines(),
            fromfile='expected',
            tofile='result',
            lineterm=''
        ):
            print(line)
        print("--- DIFF END ---\n")

    assert result == expected_output
