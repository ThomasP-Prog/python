"""Import the standard Python math module. Write a function circle_stats(radius) that takes a radius as input. 
   Inside the function, use math.pi and the radius to calculate and return both the area (A=πr2) and 
   the circumference (C=2πr) as a tuple (area, circumference). Handle negative radius appropriately (e.g., return None).
   Function Signature Idea: def circle_stats(radius): ..."""


from math import pi
from typing import Tuple,Optional

def circle_stats(radius : int) -> Optional[tuple[float,float]]:
    """
    Calculate the area and circumference of a circle

    Args:
        radius : int

    Returns:
        Optional[tuple[float,float]]
    """
    if radius < 0:
        return None

    area = pi*radius**2
    circumference = 2*pi*radius
    return area,circumference

def main() -> None:
    """main function"""

    # Test the function
    stats = circle_stats(5)
    if stats:
        # Example formatting
        print(f"For radius 5:")
        print(f"  Area: {stats[0]:.4f}")
        print(f"  Circumference: {stats[1]:.4f}")

    stats_neg = circle_stats(-1)
    print(f"For radius -1: {stats_neg}")

    # Expected Output (approx):
    # For radius 5:
    #   Area: 78.5398
    #   Circumference: 31.4159
    # For radius -1: None

if __name__ == "__main__":
    main()