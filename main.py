import sys
from stats import get_num_words
from stats import count_chars
from stats import book_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path) as f:
        file_contents = f.read()

    word_count = get_num_words(file_contents)
    char_counts = count_chars(file_contents)
    book_report(book_path, word_count, char_counts)


if __name__ == "__main__":
    main()
