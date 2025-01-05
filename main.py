def sort_and_print(characters: dict):
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))

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

def word_counter(sentence: str) -> list:
    words = sentence.split()
    print(f"Number of words:{len(words)}")
    return words

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_counter(file_contents)
        characters = character_counter(words)
        sort_and_print(characters)

main()