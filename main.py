def character_counter(words: list):
    for word in words:
        individual_characters = list(word.lower())

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