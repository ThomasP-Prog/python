"""Describe main.py: This file should import both user_interface and version_info modules. 
   It should call user_interface.display_greeting("Admin") and version_info.print_version().
   Sample Data: (No explicit data file, exercise involves calling the functions as described)."""

import user_interface,version_info

def main() -> None:
    """main function"""
    user_interface.display_greeting("Admin")
    version_info.print_version()

if __name__ == "__main__":
    main()