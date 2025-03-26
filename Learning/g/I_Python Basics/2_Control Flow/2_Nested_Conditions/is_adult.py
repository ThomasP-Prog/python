def get_age() -> int:
    """Prompt user to enter age and validate"""
    while True:
        try:
            age = float(input("Enter your age : "))
            if not age.is_integer() or age <= 0 or age > 100:
                print("Invalid input. Enter a whole number between 0 and 100")
                continue
            return int(age)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("You have exited the program, goodbye")
            exit()

def check_age(age :int) -> None:
    """Check age and print accordingly"""
    if age > 18:
        print("You are an adult.")
    elif age == 18:
        print("You just became an adult!")
    else:
        print("You are a minor.")

def main() -> None:
    """main function"""
    age = get_age()
    check_age(age)

if __name__ == "__main__":
    main()