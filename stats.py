def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    book_text = book_text.lower()

    char_counts = {}

    for char in book_text:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts
