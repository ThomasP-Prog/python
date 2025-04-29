"""Create a module with functions for handling user data. The main script should import the module using an alias, 
   get input from the user, and use the module's functions to process and display information.
   - Module File (user_utils.py):
        Define a function that takes name (string) and birth_year (integer) and returns a formatted string like "User: [Name] (Born: [Year])".
        Define another function that takes birth_year (integer) and returns True if the calculated age 
        (current year - birth year) is 18 or greater, False otherwise. (You might need to import datetime inside this module to get the current year).

    - Main Script (profile.py): Import the user_utils module using an alias (e.g., uu). 
    Prompt the user to enter their name and birth year. Use error handling (e.g., try-except ValueError) 
    to ensure the year is entered as a number. Use the functions from your aliased module (uu) to determine 
    if the user is 18 or older and to print their formatted information string.
    - Expected Output: The script should interact with the user, handle potential non-numeric year input, 
    and print messages like "User is 18 or older: True" and "User: Alice (Born: 1995)". (Note: You'll need to get the current year for the age check)."""

import user_utils as uu
import datetime as dt

def main() -> None:
    """main function"""

    name = input("enter your name : ").strip()

    try:
        birth_year_str = input("Enter your year of birth : ")
        birth_year = int(birth_year_str)
        current_year = dt.date.today().year
        if birth_year > current_year:
            raise ValueError(f"Year of birth cannot be in the future : {current_year}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(uu.format_person(name,birth_year))
        is_adult = uu.is_adult(birth_year)
        print(f"User is 18 or older: {is_adult}")
    
if __name__ == "__main__":
    main()