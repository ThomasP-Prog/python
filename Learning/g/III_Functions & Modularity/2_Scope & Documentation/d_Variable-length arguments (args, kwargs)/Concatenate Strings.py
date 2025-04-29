"""Write a function join_strings(*strings, separator=" ") that takes any number of string arguments 
   and joins them together using the provided separator (which defaults to a space)."""

def join_strings(*strings, separator=" ") -> str:
    """
    Joins any number of strings given with a separator

    Args:
        *strings (str) : variable number of string

    Returns:
        joined_string (str,optional) : joined string arguments
    """
    return separator.join(strings)

def main() -> None:
    """main function"""
    print(join_strings("Red", "Green", "Blue"))
    #Expected Output 1: Red Green Blue
    print(join_strings("Code", "Sleep", "Repeat", separator=" - "))
    #Expected Output 2: Code - Sleep - Repeat
    print(join_strings("OnlyOne"))
    #Expected Output 3: OnlyOne

if __name__ == "__main__":
    main()