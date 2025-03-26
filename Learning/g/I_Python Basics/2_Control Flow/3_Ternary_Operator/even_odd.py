def number_parity(number : int) -> str:
    """check if number is even or odd"""
    parity = "even" if (number%2 == 0) else "odd"
    return parity

def get_number() -> int:
    """prompt user to enter an int and validate"""
    while True:
        try:
            number = float(input("Enter a whole number : "))
            if number.is_integer():
                return int(number)
            else:
                print("Error, number is a float")
        except ValueError:
            print("Wrong entry, number need to be whole")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()

def main() -> None:
    """main function"""
    number = get_number()
    parity = number_parity(number)
    print(f"{number} is an {parity} number.")

if __name__ == "__main__":
    main()