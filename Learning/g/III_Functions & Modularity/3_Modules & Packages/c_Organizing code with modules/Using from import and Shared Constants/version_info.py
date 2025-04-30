"""Describe version_info.py: This file should use from config import APP_VERSION. 
   It should contain a function print_version() that prints "Application Version: " followed by the APP_VERSION."""

from config import APP_VERSION

def print_version() -> None:
    """
    print the version

    Returns:
        None
    """
    print(f"Application Version : {APP_VERSION}")

if __name__ == "__main__":
    pass