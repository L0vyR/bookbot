import sys
from stats import PrintReport

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# File path input
book_path = sys.argv[1]

# Welcome Message
print("============ BOOKBOT ============")

# Print report
PrintReport(book_path)