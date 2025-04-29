"""Define a function calculate_power that takes two parameters: base and exponent. 
   Provide a default value of 2 for the exponent. The function should calculate base raised 
   to the power of exponent (using **) and return the result. Call the function in two ways: 
   once providing only the base (to calculate the square), and once providing both base and exponent. 
   Print the results.

   Concepts Reinforced: Default argument value, returning a calculation, calling with/without optional argument."""


def calculate_power(base : int, exponent : int = 2) -> int:
    """
    Calculate base raised to the power of exponent

    Args:
        base : base number
        exponent : exponent number

    Returns:
        base to the power of exponent
    """
    return base**exponent



def main() -> None:
    """main function"""

    try:
        result_square = calculate_power(5) # Expected: 25
        print(result_square)
        result_cube = calculate_power(5, 3) # Expected: 125
        print(result_cube)
        result_zero = calculate_power(0,-2)
        print(result_zero)
    except ZeroDivisionError as e:
        print(f"Error calculating 0**2: {e}")

if __name__ == "__main__":
    main()