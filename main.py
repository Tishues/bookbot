def main():
    bookpath = "books/frankenstein.txt"
    text = get_booktext(bookpath)
    wordcount = get_wordcount(text)
    lettercounts = get_lettercount(text)
    print(f"Word count: {wordcount}")

def get_booktext(path):
    with open(path) as f:
        return f.read()
    
def get_wordcount(book):
    words = book.split()
    return len(words)

def get_lettercount(text):
    text = text.lower()
    lettercount = {}
    for letter in text:
        if letter in lettercount:
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1
    return lettercount

main()