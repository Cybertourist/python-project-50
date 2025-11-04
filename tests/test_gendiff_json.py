import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    result = generate_diff(file1, file2, format_name='json')
    assert isinstance(result, str)
