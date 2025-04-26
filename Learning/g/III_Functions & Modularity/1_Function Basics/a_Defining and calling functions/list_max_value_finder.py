"""Define a function named find_max_value that takes a single argument: data_list 
   (which you can assume is a non-empty list of numbers). Inside the function, 
   iterate through the list to find the maximum value. Return the maximum value found. 
   Call the function with a sample list and print the result. 
   (Do not use the built-in max() function for this exercise - implement the logic yourself using a loop).

   Concepts Reinforced: Function definition, list parameter, iteration (for loop) inside function, 
   conditional logic (if) inside function, variable updates inside function, return statement."""

def find_max_value(data_list : list[int]) -> int:
    """return the max value of a list of numbers"""
    if not data_list:
        raise ValueError("Empty list")

    maxi = float('-inf')
    for number in data_list:
        if number > maxi:
            maxi = number

    return maxi


def main() -> None:
    """main function"""

    max_val = find_max_value([1, 8, 3, 12, 5])
    print(max_val)

if __name__ == "__main__":
    main()