def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string
def main():
    book_string = get_book_text("books/frankenstein.txt")
    from stats import get_num_words, get_charectors_dict, char_dict_list, sort_on
    wordcount = get_num_words(book_string)
    charector_dict = get_charectors_dict(book_string)
    sort_list = char_dict_list(charector_dict)
    sort_list.sort(reverse=True, key=sort_on)
    print ("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print (f"Found {wordcount} total words\n--------- Character Count -------")
    for i in range(len(sort_list)) :
        charector = sort_list[i]["char"]
        if charector.isalpha() == True :
            print (f"{sort_list[i]["char"]}: {sort_list[i]["numb"]}")
    print("============= END ===============")
main()