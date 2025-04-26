def get_number(prompt :str) -> int|float:
    """Prompt user to enter a number and validate"""
    while True:
        try:
            number = float(input(prompt))
            return int(number) if number.is_integer() else number
        except ValueError:
            print("Error, Enter a number.")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye")
            exit()

def largest_number(numbers :list) -> int|float:
    """return largest number """
    #large = numbers[0] if numbers[0] >= numbers[1] and numbers[0] >= numbers[2] else (numbers[1] if numbers[1] >= numbers[2]  else numbers[2] )
    a,b,c = numbers
    return a if a >= b and a >= c else (b if b >= c else c)

def main() -> None:
    """main function"""
    #numbers = []
    #numbers.append(get_number("Enter first number : "))
    #numbers.append(get_number("Enter second number : "))
    #numbers.append(get_number("Enter third number : "))
    numbers = [get_number(f"Enter {pos} number: ") for pos in ["first", "second", "third"]]

    
    print(f"Numbers are : {numbers[0]},{numbers[1]},{numbers[2]} | largest number is {largest_number(numbers)}")

if __name__ == "__main__":
    main()