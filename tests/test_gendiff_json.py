import json
from hexlet_code.gendiff import generate_diff
from tests.utils import get_fixture_path


def test_generate_diff_json():
    """Проверяет вывод diff в формате JSON."""
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')

    result = generate_diff(file1, file2, format_name='json')
    parsed = json.loads(result)

    # diff должен быть списком словарей (основная структура)
    assert isinstance(parsed, list)
    assert all(isinstance(node, dict) for node in parsed)
    assert 'key' in parsed[0]
    assert 'status' in parsed[0]
