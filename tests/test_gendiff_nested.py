import os
<<<<<<< HEAD
=======
import difflib
>>>>>>> 98963a6 (Hope last upd)
from gendiff import generate_diff


def get_fixture_path(filename):
<<<<<<< HEAD
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)
=======
    """Возвращает путь к файлу из папки fixtures."""
    return os.path.join(os.path.dirname(__file__), 'test_data/fixtures', filename)
>>>>>>> 98963a6 (Hope last upd)


def test_generate_diff_nested_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = get_fixture_path('expected_stylish.txt')
    with open(expected) as f:
        expected_result = f.read()
    assert generate_diff(file1, file2, 'stylish') == expected_result
