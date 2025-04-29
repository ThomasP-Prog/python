"""Define a function describe_pet that takes pet_name (required positional argument) and 
   optionally animal_type (string, default "dog") and pet_age (integer) using keyword arguments. 
   Inside the function, print a description like "[Pet Name] is a [Animal Type].
   " If pet_age is provided (not None), also print " and is [Pet Age] years old." 
   (Hint: Use None as the default for pet_age and check if it's not None inside the function). 
   Call the function using various combinations of positional and keyword arguments.

   Concepts Reinforced: Required arguments, default string argument, default None argument pattern, 
   keyword arguments in call, conditional logic (if) inside function, string formatting."""

def describe_pet(pet_name : str,animal_type : str="dog",pet_age:int|None=None) -> None:
    """
    Print descirption of the pet according to the arguments
    
    Args:
        pet_name : name of the pet
        animal_type : type of the animal
        pet_age : age of the pet

    Returns:
        Print descirption of the pet
    """

    if pet_age is None:
        print(f"{pet_name} is a {animal_type}.")
    else:
        print(f"{pet_name} is a {animal_type} and is {pet_age} years old.")

def main() -> None:
    """main function"""

    describe_pet("Buddy")
    describe_pet("Lucy", animal_type="cat")
    describe_pet(pet_name="Max", pet_age=4)
    describe_pet("Daisy", pet_age=7, animal_type="rabbit")

if __name__ == "__main__":
    main()