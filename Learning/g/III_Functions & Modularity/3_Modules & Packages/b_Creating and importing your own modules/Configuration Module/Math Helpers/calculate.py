"""Create a module containing a reusable mathematical helper function. Import and use only that specific function in your main script.
   - Module File (math_helpers.py): Define a function that accepts a non-negative integer n 
   and returns its factorial (the product of all positive integers up to n, e.g., 
   factorial of 5 is 5×4×3×2×1=120). Remember factorial of 0 is 1.
   - Main Script (calculate.py): Import only the factorial function from the math_helpers module. 
   Call the function to calculate the factorial of 5 and print the result.
   - Expected Output: The script should print 120"""

from math_helpers import calculate_factorial

def main() -> None:
    """main function"""
    factorial = calculate_factorial(5)
    print(f"Factorial of 5 : {factorial}")

if __name__ == "__main__":
    main()