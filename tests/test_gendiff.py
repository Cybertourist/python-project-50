import os
from hexlet_code.gendiff import generate_diff


def test_generate_diff():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'file1.json')
    file2 = os.path.join(base_path, 'file2.json')
    expected_path = os.path.join(base_path, 'expected_diff.txt')

    with open(expected_path) as f:
        expected = f.read().strip()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected


def test_generate_diff_yaml():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'file1.yaml')
    file2 = os.path.join(base_path, 'file2.yaml')
    expected_path = os.path.join(base_path, 'expected_diff.txt')

    with open(expected_path) as f:
        expected = f.read().strip()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected
