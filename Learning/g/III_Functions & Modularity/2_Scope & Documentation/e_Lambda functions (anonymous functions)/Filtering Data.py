"""Create a list of names: names = ["Alice", "Bob", "Charlie", "David", "Eve"]
   Use filter and a lambda function to create a new list containing only the names that start with the letter 'A' or 'E'"""

def main() -> None:
    """main function"""

    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    new_names = list(filter(lambda x : x.startswith('A') or x.startswith('E'),names))
    print(new_names)
    # print(list(result))
    # Expected: ['Alice', 'Eve']

if __name__ == "__main__":
    main()