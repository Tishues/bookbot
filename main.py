def main():
    bookpath = "books/frankenstein.txt"
    text = get_booktext(bookpath)
    print(text)

def get_booktext(path):
    with open(path) as f:
        return f.read()

main()