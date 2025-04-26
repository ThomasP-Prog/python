def length_of_words(words : list) -> list:
    if not words:
        return []
    
    try:
        return [len(word) for word in words]
    except TypeError:
        raise TypeError("Input must be a list of strings")
    
def main() -> None:
    word_lists = [
        ["bonjour", "comment", "ça", "va", "?"],
        [],  # Empty list
        [1,2,3]
    ]
    for words in word_lists:
        try:
            lengths = length_of_words(words)
            print(f"Words: {words}")
            print(f"Lengths: {lengths}\n")
        except TypeError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()