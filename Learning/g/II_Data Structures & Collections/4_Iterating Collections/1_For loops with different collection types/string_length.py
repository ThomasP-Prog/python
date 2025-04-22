"""Write a function process_and_filter_strings that takes a list of strings as input. 
   The function should use a for loop to iterate through the list. For each string:
   - Convert the string to lowercase.
   - Check if the lowercase string starts with the letter 'a'.
   - If the string starts with 'a', calculate the length of the lowercase string.
   - Append this length to a new list.
   The function should return the new list containing the lengths of the strings that originally started with 'a' (case-insensitive)."""


def process_and_filter_strings(string_list : list[str]) -> list[int]:
    """return lenght of strings starting with 'a'"""

    word_length = []

    for string in string_list:
        if not isinstance(string,str):
            continue
        lower_string = string.lower()
        if lower_string.startswith('a'):
            word_length.append(len(lower_string))

    return word_length


def main() -> None:

    string_list = ["apple", "Banana", "avocado", "Date", "ARTICHOKE", "elderberry", "a1", " Ant ", "a"]
    # Expected output for this data: [5, 7, 9, 2, 5, 1]
    word_length = process_and_filter_strings(string_list)
    print(word_length)


if __name__ == "__main__":
    main()