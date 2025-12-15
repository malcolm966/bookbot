from stats import get_number_of_words,count_characters,get_book_text,get_characters_count_sort_by_count
import sys



def main():
    print(f'Usage: python3 main.py <path_to_book>')
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_number_of_words(book_text)
    characters_count_sort_by_count = get_characters_count_sort_by_count(book_text)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in characters_count_sort_by_count:
        print(f'{i['char']}:{i['num']}')
    print('============= END ===============')


main()