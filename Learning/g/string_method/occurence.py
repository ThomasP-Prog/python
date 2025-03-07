import re

def print_occurence(sentence :str,occurence :str) -> None:
    """Print the number of occurence in a sentence"""
    words = re.findall(r"\b\w+\b", sentence.lower())
    count = words.count(occurence.lower())
    print(f"'{sentence}' -> {count} occurence of '{occurence}'")

def get_occurence() -> str:
    """Prompt user to enter the word to count"""
    while True:
        try:
            occurence = input("Enter the word you want to count : ")
            if not occurence:
                print("Word can't be empty.")
                continue
            if " " in occurence:
                print("Word can't countain spaces.")
                continue
            else:
                return occurence
        except KeyboardInterrupt:
            print("You stopped the program, goodbye")
            exit()

def get_sentence() -> str:
    """Prompt user to enter a sentence to review"""
    while True:
        try:
            sentence = input("Enter your sentence :")
            if not sentence:
                print("Sentence can't be empty.")
                continue
            else:
                return sentence
        except KeyboardInterrupt:
            print("You stopped the program, goodbey")
            exit()

def main() -> None:
    """main function"""
    sentence = get_sentence()
    occurence = get_occurence()
    print_occurence(sentence,occurence)

if __name__ == "__main__":
    main()