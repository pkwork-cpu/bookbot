def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content
def main():
    booktext = get_book_text("books/frankenstein.txt")
    from stats import get_num_words
    wordcount = get_num_words(booktext)
    print (f"{wordcount} words found in the document")
main()