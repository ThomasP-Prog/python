def get_number() -> int:
    """Prompt user to enter a number"""
    while True:
        try:
            number = float(input("Enter a number : "))
            if number.is_integer():
                return int(number)
            else:
                print("Invalid input. Enter an integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("You have exited the program, goodbye")
            exit()

def is_multiple(number :int) -> None:
    """check is number is multilple of 5,3 or both"""
    if number%5 ==0 and number%3 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    elif number == 0:
        print("FizzBuzz (but it's zero!)")
    else:
        print(number)

def main() -> None:
    number = get_number()
    is_multiple(number)

if __name__ == "__main__":
    main()