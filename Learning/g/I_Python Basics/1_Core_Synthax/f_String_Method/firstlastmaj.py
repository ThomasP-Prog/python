def capitalize_name(full_name: str) -> str:
    """Capitalize first and last name"""
    return " ".join(word.capitalize() for word in full_name.split())
def get_name() -> str:
    while True:
        try:
            name = input("Enter your full name : ")
            if not name:
                print("Name can't be empty.")
                continue
            if not all(word.replace("-","").isalpha() for word in name.split()):
                print("Names cannot contain numbers or special characters (except hyphens).")
                continue
            if not " " in name.strip():
                print("Need a space between first and last name")
                continue
            else:
                return name
        except KeyboardInterrupt:
            print("You stopped the program, goodbye")
            exit()

def main() -> None:
    """main function"""
    name = get_name()
    name = capitalize_name(name)
    print(f"You are {name}")

if __name__ == "__main__":
    main()