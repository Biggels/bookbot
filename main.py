import sys

from stats import count_characters, count_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except OSError as err:
        print(f"Error reading {book_path}: {err}")
        sys.exit(1)

    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_sorted = dict(
        sorted(char_counts.items(), key=lambda char: char[1], reverse=True)
    )

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_counts_sorted:
        if char.isalpha():
            print(f"{char}: {char_counts_sorted[char]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


if __name__ == "__main__":
    main()
