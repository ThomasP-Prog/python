def get_number() -> int|float:
    """Prompt user to enter a number and validate"""
    while True:
        try:
            number = float(input("Enter a number :").strip())
            if number.is_integer():
                return int(number)
            else:
                return number
        except ValueError:
            print("Entry not a number.")
        except KeyboardInterrupt:
            print("You have exited the program")
            exit()

def number_type(number :int|float) -> None:
    """Print if number is positive negative or zero"""
    if number > 0:
        print(f"{int(number) if float(number).is_integer() else number} is positive")
    elif number == 0:
        print(f"{int(number) if float(number).is_integer() else number} is zero")
    else:
        print(f"{int(number) if float(number).is_integer() else number} is negative")

def main() -> None:
    """main function"""
    number = get_number()
    number_type(number)

if __name__ == "__main__":
    main()
