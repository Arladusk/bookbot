# Makes a sorted list by key value in reverse, then prints relevant result of the program, with some fluff for clarity.
def sort_and_print(characters: dict, words: list):
    print(f"This is a list of all characters in the {len(words)} words in 'Frankenstein' sorted by occurrence:")
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True)) 
    for sorted_character in sorted_characters:
        print(f"{sorted_character} found {sorted_characters[sorted_character]} times.")


# This function takes a list of words, and returns a dictionary of individual lowercase letters. 
def character_counter(words: list) -> dict:
    total_characters = {}
    for word in words:
        individual_characters = list(word.lower())
        for individual_character in individual_characters:
            if individual_character in total_characters:
                total_characters[individual_character] += 1 
            else:
                total_characters[individual_character] = 1
    return total_characters

# This function takes a string and returns it as a list of words. 
def word_counter(sentence: str) -> list:
    words = sentence.split()
    return words

#Reads the book, and calls the functions to process the text. 
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_counter(file_contents)
        characters = character_counter(words)
        sort_and_print(characters, words)

main()