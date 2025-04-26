"""Create a tuple containing three strings: your first name, last name, and favorite color.
 Use tuple unpacking to assign these to three distinct variables and print each variable on a new line."""

def main() -> None:
    """main function"""
    # Packing tuple
    strings = ("Thomas","Paper","Green")
    # Unpacking tuple
    first_name, last_name, fav_color = strings

    print(first_name)
    print(last_name)
    print(fav_color)

if __name__ == "__main__":
    main()