"""Task: Write a function format_list(data) that takes a list of strings. Use enumerate to iterate through the list. 
   If the index of an item is even, convert the item to uppercase. If the index is odd, convert it to lowercase. 
   The function should return a new list with the modified strings.

   Concepts Reinforced: enumerate, lists, basic string methods (.upper(), .lower()), conditional logic (if/else, modulo %), 
   function definition, returning a value."""

def format_list(data : list[str]) -> list[str]:
    """return formatted list of string uppercased if even and lowercased if odd"""
    if not data:
        return list()
    
    formatted_data = [item.upper() if index%2 == 0 else item.lower() for index,item in enumerate(data)]
    return formatted_data

def main() -> None:
    """main function"""

    items = ["Apple", "Banana", "CHERRY", "date", "Elderberry"]
    # Expected Output: ['APPLE', 'banana', 'CHERRY', 'date', 'ELDERBERRY']
    formatted_items = format_list(items)
    print(formatted_items)

if __name__ == "__main__":
    main()
