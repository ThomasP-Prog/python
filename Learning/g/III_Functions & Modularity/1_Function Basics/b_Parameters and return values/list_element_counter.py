"""Define a function count_occurrences that takes two parameters: data_list (a list) and item_to_count. 
   Inside the function, count how many times item_to_count appears in data_list. 
   Return the final count (an integer). Call the function with sample lists and items, and print the results.

   Concepts Reinforced: Function definition, multiple parameters (list, item), iteration (for loop) inside function, 
   conditional logic (if) inside function, counter variable, return integer value."""

from typing import List

def count_occurrences(data_list : List[str|int], item_to_count : str|int) -> int:
    """
    Count how many times item_to_count appear in the list

    Args :
    data_list : list of int or str
    item_to_count : int or str that is counted

    Returns:
    final count
    """
    count = 0

    for item in data_list:
        if item == item_to_count:
            count +=1
    return count

def main() -> None:
    """main function"""
    list_a = ["apple", "banana", "apple", "orange", "apple"]
    count1 = count_occurrences(list_a, "apple") # Expected: 3
    print(count1)
    count2 = count_occurrences(list_a, "grape") # Expected: 0
    print(count2)
    list_b = [1, 5, 2, 5, 3, 5, 4]
    count3 = count_occurrences(list_b, 5) # Expected: 3
    print(count3)

if __name__ == "__main__":
    main()