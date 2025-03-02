def print_operation(number1 : int|float,number2 :int|float) -> None:
    """print operations between 2 numbers"""
    print(f"{number1} + {number2} = {number1+number2}")
    print(f"{number1} - {number2} = {number1-number2}")
    print(f"{number1} * {number2} = {number1*number2}")
    if number2 != 0:
        print(f"{number1} / {number2} = {number1/number2}")
        print(f"{number1} // {number2} = {number1//number2}")
    else:
        print("Division by 0 not allowed")

def get_number() -> int|float:
    """prompt user to enter a number, validate and return it"""
    while True:
        try:
            num = float(input("Enter a number :"))
            return int(num) if num.is_integer() else num
        except ValueError:
            print("Wrong entry")

def main() -> None:
    """main funtion"""
    num1 = get_number()
    num2 = get_number()
    print_operation(num1,num2)

if __name__ == "__main__":
    main()