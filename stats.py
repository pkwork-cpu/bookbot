def get_book_text(filepath):
    # use path to file(sys.argv[1] to read and turn file into string)
    with open(filepath) as f:
        book_string = f.read()
    return book_string
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
'''
    Creat a list of dictionaries example:
    sort_list = [
    {'char': 'e', 'numb': 44538},
    {'char': 't', 'numb': 29493}
    ]
'''
def char_dict_list(char_dict):
    list= []
    for char in char_dict:
        # char_dict example: {'t': 29493, 'h': 19176,
        # char = charector and char_dict[char] = number
        list.append({"char": char, "numb": char_dict[char]})
    
    """
    to return a sorted list with out extra function:
    list.sort(key=lambda x: x["numb"], reverse=True)
    """
    return list

# A function that takes a dictionary and returns the value of the "numb" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["numb"]
