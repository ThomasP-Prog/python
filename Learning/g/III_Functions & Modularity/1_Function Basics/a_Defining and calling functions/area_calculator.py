"""Define a function named calculate_rectangle_area that takes two arguments: 
   length and width. Inside the function, calculate the area (length * width) and return the result. 
   Then, call this function with sample values (e.g., length 10, width 5) and print the returned result.

   Concepts Reinforced: Function definition (def), parameters, calculation inside function, return statement, function calling, passing arguments."""

def calculate_rectangle_area(length : float, width : float) -> float:
    """Calculate area of a rectangle (lenght*width)"""
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    result = float(length*width)
    return result

def main() -> None:
    """main function"""

    area = calculate_rectangle_area(10,-5)
    print(f"area of a rectangle 10 by 5 is {area}")

if __name__ == "__main__":
    main()