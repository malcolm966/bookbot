from stats import get_number_of_words,count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = get_number_of_words(book_text)
    print(count_characters(book_text))

main()