def get_number_of_words(book_text):
    total_words = len(book_text.split())
    return total_words

def count_characters(book_text):
    book_text = book_text.lower()
    character_dic = {}
    for c in book_text:
        if c in character_dic:
            character_dic[c] += 1
        else:
            character_dic[c] = 1
    return character_dic