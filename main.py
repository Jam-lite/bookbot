from stats import count_words, count_characters, sorted_list_of_dictionaries
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #print(get_book_text("books/frankenstein.txt"))
    num_words = count_words(get_book_text(sys.argv[1]))
    #print(f"{num_words} words found in the document")
    #print(count_characters(get_book_text("books/frankenstein.txt")))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list_of_dictionaries(count_characters(get_book_text(sys.argv[1])))
    print("============= END ===============")


main()
