
# Makes a sorted list by key value in reverse, then prints relevant result of the program, with some text for clarity.
def sort_and_print(characters: dict, words: list):
    print(f"This is a list of all characters in the {len(words)} words in 'Frankenstein' sorted by occurrence:")
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True)) 
    for sorted_character in sorted_characters:
        print(f"{sorted_character} found {sorted_characters[sorted_character]} times.")

# Takes a list of words, converts all letters into lowercase, then depending on user input it includes or excludes non-alphabetical characters. 
# Then returns a dictionary of individual characters. 
def character_counter(words: list, user_choice: str) -> dict:
    total_characters = {}
    for word in words:
        individual_characters = list(word.lower())
        for individual_character in individual_characters:
            if user_choice == "y":
                if individual_character in total_characters:
                    total_characters[individual_character] += 1 
                else:
                    total_characters[individual_character] = 1
            else:
                if individual_character in total_characters and individual_character.isalpha():
                    total_characters[individual_character] += 1 
                elif individual_character.isalpha():
                    total_characters[individual_character] = 1
    return total_characters

# Takes a string and returns it as a list of words. 
def word_counter(sentence: str) -> list:
    words = sentence.split()
    return words

# Takes user input on wether or not to keep all characters in the list.
def user_choice():
    return input("Do you want to include all characters in the resulting list, such as punctuation and numbers? (y/n):").lower()

# Takes user input, Reads the book, and calls the functions to process the text. 
def main():
    include_all_chars = user_choice()
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_counter(file_contents)
        characters = character_counter(words, include_all_chars)
        sort_and_print(characters, words)

main()