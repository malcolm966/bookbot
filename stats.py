def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

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

def get_characters_count_sort_by_count(book_text):
    result_dic = {}
    book_text = book_text.lower()
    for c in book_text:
        if c in result_dic:
            result_dic[c]['num'] += 1
        else:
            if c >= 'a' and c <= 'z':
                result_dic[c] = {"char":c, "num" : 1}
    result_list = []
    for i in result_dic:
        result_list.append(result_dic[i])
    result_list.sort(key=sort_on,reverse=True)
    return result_list

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items['num']

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)
# # [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]