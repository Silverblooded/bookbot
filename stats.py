def count():
    with open("./books/frankenstein.txt") as f:
        num_words = 0
        file_contents = f.read()
        num_words = len(file_contents.split())
        return num_words


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
        return letters


def sort_on(item):
    return item[1]


print(
    "============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt..."
)

print(f"----------- Word Count ----------\n{count()}")
letter_counts = characters_sorted()
sorted_letters = sorted(letter_counts.items(), key=sort_on, reverse=True)

print("--------- Character Count -------")
for letter, count in sorted_letters:
    print(f"{letter} | {count}")
print("============= END ===============")
