from stats import count_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)

    print(f"Found {num_words} total words")


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


if __name__ == "__main__":
    main()
