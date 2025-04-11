"""Use enumerate along with tuple unpacking in a for loop to print the index
   and the value for each item in the list data = ["apple", "banana", "cherry"].
   The output should look like "Index 0: apple", "Index 1: banana", etc."""

def print_list_with_indices(data : list[str]) -> None:
    """Format list using enumerate"""
    for index, fruit in enumerate(data):
        print(f"Index {index}: {fruit}")

def main() -> None:
    """ main function"""
    data = ["apple", "banana", "cherry"]
    print_list_with_indices(data)
    

if __name__ == "__main__":
    main()