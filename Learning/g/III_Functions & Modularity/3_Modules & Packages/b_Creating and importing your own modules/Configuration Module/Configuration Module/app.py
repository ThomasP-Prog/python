"""Create a module that stores configuration settings. Create a main script that imports this module and prints the settings.
   - Module File (config.py): Define at least two variables, for example, WEBSITE_URL = "http://example.com" and TIMEOUT = 30.
   - Main Script (app.py): Import the entire config module. Print the values of WEBSITE_URL and TIMEOUT using the config. prefix.
   - Expected Output: The script should print the URL string and the integer 30."""

import config

def main() -> None:
    """main function"""
    print(f"URL : {config.WEBSITE_URL}")
    print(f"Timeout : {config.TIMEOUT}")

if __name__ == "__main__":
    main()