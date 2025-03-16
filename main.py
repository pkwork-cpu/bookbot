def main():
    # import command-line argument script name and path to book
    import sys
    # if path to file is not specified will prompt instruction on how to use program
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # import data analysis functions from stats.py
    from stats import get_book_text, get_num_words, get_charectors_dict, char_dict_list, sort_on
    # use path to file(sys.argv[1] to read and turn file into string)
    book_string = get_book_text(sys.argv[1])
    # count the number of words 
    wordcount = get_num_words(book_string)
    # Count characters save result into dictonary exmp: {'p': 6121, 'r': 20818, ect}
    charector_dict = get_charectors_dict(book_string)
    '''
    Creat a list of dictionaries example:
    sort_list = [
    {'char': 'e', 'numb': 44538},
    {'char': 't', 'numb': 29493}
    ]
    '''
    sort_list = char_dict_list(charector_dict)
    # sort list by highest used charector to least
    sort_list.sort(reverse=True, key=sort_on)
    #finally prints word count and list of charectors and number of charectors
    print ("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print (f"Found {wordcount} total words\n--------- Character Count -------")
    for i in range(len(sort_list)) :
        charector = sort_list[i]["char"]
        if charector.isalpha() == True :
            print (f"{sort_list[i]["char"]}: {sort_list[i]["numb"]}")
    print("============= END ===============")
main()