def word_counter(sentence: str) -> int:
    words = sentence.split()
    print(f"Number of words:{len(words)}")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_counter(file_contents)

main()