from stats import get_num_words
from stats import text_to_num
from stats import count_char
import sys


file_contents = ""

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    file_contents = get_book_text()
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    num_chars = text_to_num(file_contents)
    for char in count_char(num_chars):
        print (f'{char["char"]}: {char["num"]}')

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

