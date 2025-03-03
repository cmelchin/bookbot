def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file):
    book_text = get_book_text(file)
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

def get_char_count(file):
    char_used = {}
    book_text = get_book_text(file).lower()
    for i in book_text:
        for c in list(i):
            if c not in char_used:
                char_used[c] = 1
            else:
                char_used[c] += 1
    return char_used

def formatter(file):
    print("""
==================== BOOKBOT ====================
Analyzing book found at books/frankenstein.txt...
------------------ Word Count -------------------""")
    get_word_count(file)
    print("""---------------- Character Count ----------------""")
    word_count_sorted = dict(sorted(get_char_count(file).items(), key=lambda item: item[1], reverse = True))
    for i in word_count_sorted:
        print(f"{i}: {word_count_sorted[i]}")
