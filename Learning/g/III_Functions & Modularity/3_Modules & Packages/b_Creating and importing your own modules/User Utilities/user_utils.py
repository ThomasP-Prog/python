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

import datetime as dt

def format_person(name : str, birth_year : int) -> str:
    """
    make a string out of the provided info

    Args:
        name : str
        birth_year : int

    Returns:
        int
    """
    return f"User : {name} (Born : {birth_year})"

def is_adult(birth_year: int)-> bool :
    """
    Returns True if adult else False

    Args:
        birth_year : int

    Returns:
        bool
    """
    current_year = dt.date.today().year
    return current_year - birth_year >= 18
