"""
Define a simple class named Laptop with only a pass statement in its body. 
In your main function (or script area), create three different instances of this Laptop class, 
assigning them to variables laptop1, office_laptop, and gaming_laptop. 
Print the type of laptop1 and then print the unique memory IDs (using id()) of all three instances to show they are distinct.
"""

class Laptop:
    pass

def main() -> None:
    """main function"""
    laptop1 = Laptop()
    office_laptop = Laptop()
    gaming_laptop = Laptop()
    print(f"laptop1 type : {type(laptop1)}")
    print(f"laptop1 id : {id(laptop1)}")
    print(f"office_laptop id : {id(office_laptop)}")
    print(f"gaming_laptop id : {id(gaming_laptop)}")

if __name__ == "__main__":
    main()