from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
        return contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count(book_text)
main()