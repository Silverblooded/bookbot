def count():
    with open("./books/frankenstein.txt") as f:
        num_words = 0
        file_contents = f.read()
        book = file_contents.split(" ")
        for i in range(len(book)):
            num_words = i
        print(f"{num_words} words found in the document")
    # print(f"{num_words} words found in the document")


count()
