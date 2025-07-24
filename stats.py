def count():
    with open("./books/frankenstein.txt") as f:
        num_words = 0
        file_contents = f.read()
        book = file_contents.split(" ")
        num_words = len(file_contents.split())
        print(f"{num_words} words found in the document")


def characters_sorted():
    with open("./book/frankenstein.txt") as f:
        pass


count()
