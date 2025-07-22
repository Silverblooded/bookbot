file_contents = ""
num_words = None


def get_book_text(file_contents):
    words = 0
    for words in file_contents:
        words += 1
        num_words = words
        return num_words


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    file_list = file_contents.split(" ")
    get_book_text(file_list)
    print(f"{num_words} words found in the document")
