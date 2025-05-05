"""
Write a function sum_numeric_strings(values: list) -> float. 
The input values is a list containing items of potentially different types (strings, integers, floats, maybe others). 
Iterate through the list. For each item, try to convert it into a float.
    - If the conversion is successful, add it to a running total.
    - If the conversion fails (raises a ValueError), print a warning message like "Warning: Skipping non-numeric value: [item]" and use continue to move to the next item.
    - After the loop, return the total sum of successfully converted numbers
"""
from typing import List,Any

def sum_numeric_strings(values: List[Any]) -> float:
    """
    Sum the total of every numbers in the list and print a warning message for non numeric value

    Args:
        values: List[Any]
        
    Returns:
        float
    """
    total = 0
    for item in values:
        try:
            if isinstance(item,bool):
                raise ValueError
            total += float(item)
        except ValueError:
            print(f"Warning: Skipping non-numeric value: {item}")
            continue
    return total

def main() -> None:
    """main function"""

    data1 = ["10.5", "2", "-3", "abc", "7.0", True, "1"] 
    # Expected output: Prints warning for "abc", possibly for True depending on float() behavior, returns 17.5 (10.5 + 2.0 - 3.0 + 7.0 + 1.0) -- Note: float(True) is 1.0

    data2 = ["one", "two", "three"]
    # Expected output: Prints warnings for all, returns 0.0

    data3 = [1, 5, 10.0]
    # Expected output: No warnings, returns 16.0

    total1 = sum_numeric_strings(data1)
    print(f"Total 1: {total1}")
    total2 = sum_numeric_strings(data2)
    print(f"Total 2: {total2}")
    total3 = sum_numeric_strings(data3)
    print(f"Total 3: {total3}")

if __name__ == "__main__":
    main()