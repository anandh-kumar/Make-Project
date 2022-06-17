import argparse

args = [
    '--language',
    '--category',
    '--name',
    '--type'
]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="A project/program stats")
    parser.add_argument(
        '-l',
        '--language',
        dest='language',
        help='Tell mkproj language used by project/program',
        type=str,
        required=True,

    )
    parser.add_argument(
        '-c',
        '--category',
        dest='categoryName',
        help='Tell mkproj category for project/program',
        type=str,
        required=True,
        nargs='+'

    )
    parser.add_argument(
        '-n',
        '--name',
        dest='projName',
        help='Tell mkproj projName for project/program',
        type=str,
        required=True
    )
    parser.add_argument(
        '-t',
        '--type',
        dest='type',
        help='Program type large or small. default [large]',
        type=str,
        required=False
    )

    return parser.parse_args()
