from collections import Counter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_chars = count_characters(file_contents)
    # print(num_words)
    print_report(num_words, num_chars)

def count_words(text):
    words = text.split()
    word_count = Counter(words)
    # print(sum(word_count.values()))
    return sum(word_count.values())

"""
ANOTHER SOLUTION FOR WORD COUNT

def get_num_words(text):
    words = text.split()
    return len(words)

"""

def count_characters(text):
    char_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        # char is each character in lowercase_text
        # If a character is in the dictionary, add 1 to it's count.
        # If a character is not in the dictionary, add that character to the dictionary 
        # and have it's value start at 1
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def print_report(num_words, char_dict):
    char_list = []
    char_list = list(char_dict.items())
    sorted_char_list = char_list.sort()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char in char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {char_dict[char]} times")


main()