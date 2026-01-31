def main():
    print(get_book_text("books/frankenstein.txt"))


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


if __name__ == "__main__":
    main()
