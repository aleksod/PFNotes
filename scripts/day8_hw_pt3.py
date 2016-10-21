def book_word_counter(book_path):
    num_words = 0
    with open(book_path) as book:
        for line in book:
            num_words += len(line.split())
    return num_words

print book_word_counter('misc/books/flatland.txt')
print book_word_counter('misc/books/programming_languages.txt')
