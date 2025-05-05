"""
Write a function generate_random_point_in_circle(radius: float) -> tuple[float, float]. 
The function should generate a random point (x, y) that lies within or on the boundary 
of a circle centered at (0, 0) with the given radius. 
(Hint: Generate a random angle using math.pi and random.uniform(), 
generate a random distance from the center up to the radius, possibly using math.sqrt 
and random.random(), then convert polar coordinates (distance, angle) to Cartesian coordinates (x, y) using math.cos and math.sin)
"""

from random import uniform,random 
from math import cos,sin,pi,sqrt

def generate_random_point_in_circle(radius: float) -> tuple[float, float]:
    """
    Generates a random point (x, y) uniformly within a circle

    Args:
        radius : float

    Returns:
        tuple[float,float]
    """
    angle = uniform(0,2*pi)
    r = radius * sqrt(random())
    x = round(r*cos(angle),2)
    y = round(r*sin(angle),2)
    return (x,y)

def main() -> None:
    """main function"""

    # Example call:
    point1 = generate_random_point_in_circle(10.0) 
    print(point1) # Expected: A tuple like (x, y) where sqrt(x**2 + y**2) <= 10.0
    point2 = generate_random_point_in_circle(1.0) 
    print(point2) # Expected: A tuple like (x, y) where sqrt(x**2 + y**2) <= 1.0

if __name__ == "__main__":
    main()