def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content
def main():
    print (get_book_text("books/frankenstein.txt"))
main()