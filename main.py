def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_counts = get_letter_count(text)
    char_list = get_characters(letter_counts)
    print_report(char_list, word_count, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def get_characters(letter_counts):
    characters_list = [{"character": key, "count": value} for key, value in letter_counts.items() if key.isalpha()]
    characters_list.sort(key=lambda x: x["count"], reverse=True)
    return characters_list

def print_report(char_list, word_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char_info in char_list:
        character = char_info['character']
        count = char_info['count']
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

main()