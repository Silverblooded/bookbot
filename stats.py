def count():
    with open("./books/frankenstein.txt") as f:
        num_words = 0
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"{num_words} words found in the document")


def characters_sorted():
    with open("./books/frankenstein.txt") as f:
        letters = {}
        file_contents = f.read()
        book = file_contents.lower()
        for letter in book:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        print(letters)


count()
characters_sorted()
