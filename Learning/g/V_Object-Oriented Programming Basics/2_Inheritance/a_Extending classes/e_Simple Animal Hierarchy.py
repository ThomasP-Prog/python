"""
Create a base class Animal with an __init__(self, name: str) that stores the name and a method speak(self) that prints a generic sound like "[Name] makes a sound."
Create a subclass Cat that inherits from Animal. Its __init__ should take name and call the parent's __init__. Override the speak(self) method in Cat to print "[Name] meows."
Create instances of Animal and Cat and call their speak() methods.

Sample Data: No external data needed. Test with names like "Generic" for Animal and "Whiskers" for Cat.
"""

" --- Superclass ---"
class Animal:
    def __init__(self, name:str) -> None:
        """Initialize Animal"""
        self.name = name
    
    def speak(self) -> None:
        """Print animal sound"""
        print(f"{self.name} makes a sound.")

" --- Subclass ---"
class Cat(Animal):
    def __init__(self, name:str) -> None:
        """Initialize cat"""
        super().__init__(name)

    def speak(self) -> None:
        """Override Animal speak()"""
        print(f"{self.name} meows.")

def main() -> None:
    """main function"""
    animal1 = Animal("Generic")
    cat1 = Cat("Whiskers")
    animal1.speak()
    cat1.speak()

if __name__ == "__main__":
    main()