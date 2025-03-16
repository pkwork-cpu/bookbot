def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string
def main():
    book_string = get_book_text("books/frankenstein.txt")
    from stats import get_num_words
    from stats import get_charectors_dict
    wordcount = get_num_words(book_string)
    charector_dict = get_charectors_dict(book_string)
    print (f"{wordcount} words found in the document\n\nCharector count:\n{charector_dict}")

main()