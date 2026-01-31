from stats import count_characters, count_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_sorted = dict(
        sorted(char_counts.items(), key=lambda char: char[1], reverse=True)
    )

    print(f"Found {num_words} total words")
    print(char_counts_sorted)


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


if __name__ == "__main__":
    main()
