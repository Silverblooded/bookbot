from stats import count, characters_sorted, sort_on
import sys


def open():
    if len(sys.argv) < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
