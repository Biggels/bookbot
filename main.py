from stats import count_characters, count_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_sorted = dict(
        sorted(char_counts.items(), key=lambda char: char[1], reverse=True)
    )

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
