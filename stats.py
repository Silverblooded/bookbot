def count(filename):
    with open(filename, "r") as f:
        num_words = 0
        file_contents = f.read()
        num_words = len(file_contents.split())
        return num_words


def characters_sorted(filename):
    with open(filename, "r") as f:
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


def out(filename):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filename}...")

    print(f"----------- Word Count ----------\nFound {count(filename)} total words")
    letter_counts = characters_sorted(filename)
    sorted_letters = sorted(letter_counts.items(), key=sort_on, reverse=True)

    print("--------- Character Count -------")
    for letter, letter_count in sorted_letters:
        print(f"{letter}: {letter_count}")
    print("============= END ===============")
