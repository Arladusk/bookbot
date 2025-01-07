# Takes user input on wether or not to keep all characters in the list.
def user_choice() -> str:
    return input("Do you want to include all characters in the resulting list, such as punctuation and numbers? (y/n):").lower()

# Takes a string and returns it as a list of words. 
def word_counter(sentence: str) -> list:
    words = sentence.split()
    return words

# Turns list of words into list of individual lowercase characters.
def lower_case(words: list) -> list:
    individual_characters = []
    for word in words:
        individual_characters.extend(list(word.lower()))
    return individual_characters

# Filters based on user input and calls add_character
def filter_character(raw_characters: list, user_choice: str) -> dict:
    total_characters = {} 
    for raw_character in raw_characters:
        if user_choice == "y" or (user_choice == "n" and raw_character.isalpha()):
            increment_character_count(total_characters, raw_character)
    return total_characters

    # Adds new characters to dict, increments if duplicate.  
def increment_character_count(total_characters: dict, character: str) -> dict:
    if character in total_characters: 
        total_characters[character] += 1
    else:
        total_characters[character] = 1

# Makes a sorted list by key value in reverse, then prints relevant result of the program, with some text for clarity.
def sort_and_print(characters: dict, words: list):
    print(f"This is a list of all characters in the {len(words)} words in 'Frankenstein' sorted by occurrence:")
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True)) 
    for sorted_character in sorted_characters:
        print(f"{sorted_character} found {sorted_characters[sorted_character]} times.")

# Reads the book, and calls the functions to process and print the results of the book.. 
def main():
    include_all_chars = user_choice()
    with open("books/testbook.txt") as f:
        file_contents = f.read()
        words = word_counter(file_contents)
        characters = lower_case(words)
        counted_characters = filter_character(characters, include_all_chars)
        sort_and_print(counted_characters, words)

main()