def get_num_words(books_text_string):
    # Split String word by word and store in list
    list_of_words = books_text_string.split()
    # return the number of items in list
    return  len(list_of_words)



def get_charectors_dict(books_text_string):
    all_low = books_text_string.lower()
    # Initialize an empty dictionary to store character counts
    char_count = {}
    # Count characters, save into dictonary and return dict
    for char in all_low:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count