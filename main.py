def character_counter(words: list):
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
        character_counter(words)
main()