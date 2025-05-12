"""
Define a class Vehicle.

    Add a class variable number_of_wheels = 4.
    In its __init__, accept color (string) and make (string) as arguments and store them as instance attributes.
    Add a method display_details() that prints the vehicle's make, color, and its number_of_wheels.

Sample Usage: Create two Vehicle instances with different colors and makes. Call display_details() on both. 
Then, change Vehicle.number_of_wheels to 3 and call display_details() on both instances again to see the change.
"""

class Vehicle:
    number_of_wheels = 4
    def __init__(self, color:str, make:str) -> None:
        """Initialize the Vehicle"""
        self.color = color
        self.make = make
    def display_details(self) -> None:
        """Prints the vehicule info"""
        print(f"Vehicle make : {self.make}, color : {self.color}, number of wheels : {self.number_of_wheels}")

def main() -> None:
    """main function"""
    veh1 = Vehicle("blue","Toyota")
    veh2 = Vehicle("red","Ferrari")
    veh1.display_details()
    veh2.display_details()
    veh1.number_of_wheels = 3
    veh1.display_details()
    veh2.display_details()

if __name__ == "__main__":
    main()