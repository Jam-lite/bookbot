def count_words(file_contents):
    list_of_words = file_contents.split(sep=None)
    num_of_words = 0
    
    for word in list_of_words:
        num_of_words += 1
    
    return num_of_words

def count_characters(file_contents):
    character_dictionary = {}

    file_text = file_contents.lower()

    for char in file_text:

        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char]=1
    
    return character_dictionary

def sort_on(dict):
    return dict["num"]

def sorted_list_of_dictionaries(input_dictionary):
    
    char_list = [{"char": char, "num": count} for char,count in input_dictionary.items()]

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))
        else:
            pass


