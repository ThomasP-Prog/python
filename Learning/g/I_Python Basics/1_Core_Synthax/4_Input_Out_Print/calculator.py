def get_number() -> int|float:
    """Prompt user to enter a number, validate and return it"""
    while True:
        try:
            number = float(input("Enter a number : "))
            return int(number) if number.is_integer() else number
        except ValueError:
            print("Wrong entry")

def print_calculus(num1 :float|int, num2 :float|int) -> None:
    """print + - * and / if possible"""
    print(f"{num1} + {num2} = {num1+num2}")
    print(f"{num1} - {num2} = {num1-num2}")
    print(f"{num1} * {num2} = {num1*num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("Skipping division: Cannot divide by zero.")

def main() -> None:
    """main funtion"""
    num1 = get_number()
    num2 = get_number()
    print_calculus(num1,num2)

if __name__ == "__main__":
    main()