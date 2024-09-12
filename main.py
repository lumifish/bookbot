def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    d_contents = {}
    lowercase_words = text.lower().split()
    for word in lowercase_words:
        for letter in word:
            if letter in d_contents and letter.isalpha():
                d_contents[letter] +=1
            elif letter.isalpha():
                d_contents[letter] =1
    return d_contents

def get_word_count(text):
    return len(text.split())

def dict_to_list(dict):
    list = []
    for i in dict:
        list.append({"letter":i,"num" : dict[i]})
        list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["num"]

def print_report(book_path, word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    letter_list = dict_to_list(letter_count)
    for letter in letter_list:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    letter_count = get_letter_count(book)
    print_report(book_path, word_count, letter_count)
    
main()