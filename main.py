import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f):
    with open(f) as book_file:
        file_contents = book_file.read()
    return file_contents

from stats import num_words

from stats import num_characters

from stats import convert_to_list

from stats import sort_on

def main():
    book_text = get_book_text(sys.argv[1])
    count = num_words(book_text)
    print(f"Found {count} total words")
    char = num_characters(book_text)
    convert = convert_to_list(char)
    convert.sort(reverse=True, key=sort_on)
    for k in convert:
        character = k["char"]
        if character.isalpha():
            count = k["num"]
            print(f"{character}: {count}")

main()
