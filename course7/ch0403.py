def print_chars(word, i):
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)




print_chars('elephant', 3)