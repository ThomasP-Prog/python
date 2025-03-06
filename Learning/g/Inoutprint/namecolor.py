def get_input(prompt :str) -> str:
    """Prompt user for input with validation"""
    while True:
        value = input(prompt).strip().lower()
        if value:
            return value
        print("Inpur cannot be empty.")

def print_name_color(name :str, color :str) -> None:
    """print name end favorite color"""
    print(f"Your name is {name} and your favorite color is {color}")

def main() -> None:
    """main function"""
    name = get_input("Enter your name : ").title()
    fav_color = get_input("Enter your favorite color :")
    print_name_color(name,fav_color)

if __name__ == "__main__":
    main()