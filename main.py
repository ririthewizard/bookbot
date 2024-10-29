def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_appearances(text)
    sorted = print_report(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    #print(chars_dict)
    for char in sorted:
        print(f"The '{char["character"]}' character was found {char["num"]} times")


def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_character_appearances(text):
    character_dict = {}
    for char in text:
        c = char.lower()
        if c not in character_dict and c.isalpha():
            character_dict[c] = 1
        elif c.isalpha():
            character_dict[c] += 1
    #print(character_dict)
    return character_dict
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def print_report(dict):
    tmp = []
    for key in dict.keys():
        tmp = [{"character": k, "num": v} for k,v in dict.items()]
    tmp.sort(reverse=True, key=sort_on)
    print(type(tmp))
    return tmp



main()
