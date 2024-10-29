def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

    def wordsInBook():
        book_string = file_contents.split()
        print(len(book_string))
        return len(book_string)
    
    wordsInBook()


main()
