from stats import count, characters_sorted, sort_on, out
import sys


def open():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        out(filename)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


open()
