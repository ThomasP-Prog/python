"""Write a function process_and_filter_strings that takes a list of strings as input. 
   The function should use a for loop to iterate through the list. For each string:
   - Convert the string to lowercase.
   - Check if the lowercase string starts with the letter 'a'.
   - If the string starts with 'a', calculate the length of the lowercase string.
   - Append this length to a new list.
   The function should return the new list containing the lengths of the strings that originally started with 'a' (case-insensitive)."""


def main() -> None:

    string_list = ["apple", "banana", "cherry", "date"]
    # Expected output for this data: [5, 6, 6, 4]


if __name__ == "__main__":
    main()