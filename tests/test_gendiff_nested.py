import os
import difflib
from gendiff.gendiff import generate_diff


def get_fixture_path(filename):
    """Возвращает путь к файлу из папки fixtures."""
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def test_generate_diff_nested_json():
    """Тестирует сравнение вложенных структур JSON в формате 'stylish'."""
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = get_fixture_path('expected_stylish.txt')

    with open(expected) as f:
        expected_output = f.read().strip()

    result = generate_diff(file1, file2, format_name='stylish').strip()

    # Если есть различия — выводим diff для отладки
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
