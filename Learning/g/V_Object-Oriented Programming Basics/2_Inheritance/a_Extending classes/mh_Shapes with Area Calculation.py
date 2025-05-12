"""
Create a base class Shape with an __init__(self, color: str) and a method get_color(self) -> str. 
It should also have a method calculate_area(self) that raise NotImplementedError (because a generic shape doesn't have a specific area formula).
Create a subclass Rectangle inheriting from Shape. 
Its __init__ should take color, width, and height. 
Store width and height. Implement calculate_area(self) to return width * height.
Create a subclass Triangle inheriting from Shape. 
Its __init__ should take color, base, and height. Store base and height. 
Implement calculate_area(self) to return 0.5 * base * height.

Sample Usage: Create a Rectangle and a Triangle. Print their color and calculated area. 
Try calling calculate_area() on a direct Shape instance within a try...except NotImplementedError block.
"""

from typing import Any

# --- Superclass ---
class Shape:
    def __init__(self,color:str):
        """Initialize Shape"""
        self.color = color

    def get_color(self) -> str:
        """Returns the color of the shape"""
        return self.color
    
    def calculate_area(self) -> Any:
        raise NotImplementedError("The generic shape as no formula.")

# --- Subclass of Shape ---
class Rectangle(Shape):
    def __init__(self, color:str, width:float, height:float):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

# --- Subclass of Shape ---
class Triangle(Shape):
    def __init__(self,color:str, base:float, height:float):
        super().__init__(color)
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height
    
def main() -> None:
    """main function"""
    rectangle1 = Rectangle("blue",10,5)
    triangle1 = Triangle("red",3.5,8)
    print(f"rectangle1 color : {rectangle1.get_color()}, area : {rectangle1.calculate_area()}")
    print(f"triangle1 color : {triangle1.get_color()}, area : {triangle1.calculate_area()}")
    weird_shape = Shape("green")
    try:
        print(f"weird_shape color : {weird_shape.get_color()}, area : {weird_shape.calculate_area()}")
    except NotImplementedError as e:
        print(f"Error, {e}")

if __name__ == "__main__":
    main()