"""
Take your solution code for Exercise 1 from the previous section (calculate_ratio). Modify it to:

    Add an else block that prints "Calculation successful." only when the division succeeds.
    Add a finally block that always prints "Ratio calculation attempt finished.".
"""

from typing import Optional

def calculate_ratio(numerator : int, denominator : int) -> Optional[float]:
    """
    Calculate the ratio of numerator / denominator

    Args:
        numerator : int
        denominator : int

    Returns:
        Optional[float]
    """
    ratio = None
    try:
        ratio = numerator / denominator
    except ZeroDivisionError:
        print("Error : Denominator cannot be zero")
    else:
        print("Calculation successful.")
    finally:
        print("Ratio calculation attempt finished.")

    return ratio

def main() -> None:
    """main function"""

    result1 = calculate_ratio(10, 2) # Expected: 5.0
    result2 = calculate_ratio(5, 0)  # Expected: Prints error, returns None
    result3 = calculate_ratio(0, 5)  # Expected: 0.0
    print(result1, result2, result3)

if __name__ == "__main__":
    main()