"""The main routine of sudoku."""

import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print(args)

if __name__ == "__main__":
    main()
