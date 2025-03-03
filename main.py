import sys
from stats import formatter

file = sys.argv[1]

if len(sys.argv) < 2:
    print("Useage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    formatter(file)
