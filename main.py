def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_appearances(text)
    print_report(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    #print(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_character_appearances(text):
    character_dict = {}
    for char in text:
        c = char.lower()
        if c not in character_dict:
            character_dict[c] = 1
        else:
            character_dict[c] += 1
    #print(character_dict)
    return character_dict
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(dict):
    tmp = []
    for key, value in dict.items():
        if key.isalpha():
            tmp.append({key, value})
    for d in tmp:
        d.type()
        print(f"The /'{d[0]}' was found /'{d[1]}' times")



main()
