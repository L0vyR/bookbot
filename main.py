import sys
from stats import WordsCounter
from stats import CharacterCounter
from stats import PrintReport

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

#def main():
#    print(get_book_text("/home/sweery/workspace/github.com/bookbot/books/frankenstein.txt"))


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")

WordsCounter(get_book_text(book_path))

PrintReport(CharacterCounter(get_book_text(book_path)))