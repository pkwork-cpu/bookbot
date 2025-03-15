def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content
def count_words(book_text_string):
    list_of_words = book_text_string.split()
    return  len(list_of_words)
def main():
    booktext = get_book_text("books/frankenstein.txt")
    wordcount = count_words(booktext)
    print (f"{wordcount} words found in the document")
main()