class NotOperator(Exception):
    """Raised when user doesn't enter + - * / when needed"""
    pass

def get_number() -> int|float:
    """Prompt user to enter a number and validate"""
    while True:
        try:
            number = float(input("Enter a number : "))
            return int(number) if number.is_integer() else number
        except ValueError:
            print("Error. Enter a number")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye")
            exit()

def calculus(num1 :int|float) -> int|float|None:
    """Prompt user to enter an operator, validate and ask for a seconde number then do the calculus"""
    while True:
        try:
            result = input("Enter the operator : ")
            if not (result =="/" or result =="*" or result =="+" or result =="-"):
                raise NotOperator(result)
            print(f"{num1} {result}")
            num2 = get_number()
            if result == "+":
                result = num1+num2
                print(f"{num1} + {num2} = {result}")
            elif result == "-":
                result = num1-num2
                print(f"{num1} - {num2} = {result}")
            elif result == "*":
                result = num1*num2
                print(f"{num1} / {num2} = {result}")
            else:
                if num2 != 0:
                    result = num1/num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error. Division by 0")
                    return None

            return int(result) if float(result).is_integer() else float(result)
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()
        except NotOperator:
            print("Enter +,-,* or /")
