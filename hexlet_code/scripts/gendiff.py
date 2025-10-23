import argparse
from hexlet_code.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        metavar='FORMAT'
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
