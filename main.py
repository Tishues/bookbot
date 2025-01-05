def main():
    bookpath = "books/frankenstein.txt"
    text = get_booktext(bookpath)
    wordcount = get_wordcount(text)
    print(f"Word count: {wordcount}")

def get_booktext(path):
    with open(path) as f:
        return f.read()
    
def get_wordcount(text):
    words = text.split()
    return len(words)

main()