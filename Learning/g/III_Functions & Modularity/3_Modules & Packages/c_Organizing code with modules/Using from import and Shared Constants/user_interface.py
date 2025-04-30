"""Describe user_interface.py: This file should use from config import DEFAULT_GREETING 
   to import the greeting constant. It should contain a function display_greeting(name: str) 
   that prints DEFAULT_GREETING followed by the name"""

from config import DEFAULT_GREETING

def display_greeting(name : str) -> None:
    """
    Print the greeting

    Args:
        name : str

    Returns:
        None
    """
    print(f"{DEFAULT_GREETING} {name}")

if __name__ == "__main__":
    pass