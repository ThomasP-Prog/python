def get_input(prompt :str, data_type : type = str,validation_func = None) -> int|float|str:
    """Prompt user to enter a number or an operator and validate"""
    while True:
        try:
            user_input = input(prompt).strip()
            if data_type in [int,float]: # if data_tyoe is int or float
                if user_input.isdigit():
                    return int(user_input)
                else:
                    return float(user_input)
            if validation_func is not None and not validation_func(user_input): # Check custom validation
                raise ValueError("Invalid operator! Please enter one of: +, -, *, /.")                       # Here + , - , * , /
            return user_input
        except ValueError:
            if data_type in [int,float]:
                print("Error. Enter a number")
            else:
                print("Invalid operator! Please enter one of: +, -, *, /")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye")
            exit()

def calculus(num1 :int|float,num2 :int|float, operator :str) -> int|float|None:
    """Calculate based on previous entries"""
    
    if operator == "+":
        result = num1+num2
    elif operator == "-":
        result = num1-num2
    elif operator == "*":
        result = num1*num2
    else:
        if num2 != 0:
            result = num1/num2
        else:
            print("Error. Division by 0")
            return None
    print(f"{num1} {operator} {num2} = {result}")
    return int(result) if float(result).is_integer() else float(result)


def continue_calculating() -> bool|None:
    """Prompt user to enter y/n to continue calculating"""
    while True:
        try:
            next_op = input("Do you want to continue calculating ? ").strip().lower()
            if next_op == "y" or next_op == "yes":
                return True
            elif next_op == "n" or next_op == "no":
                print("\nYou exited the program. Goodbye.")
                exit()
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def keep_result(num1 :int|float,result :int|float) ->int|float|None:
    """Prompt user to enter y/n to keep previous result"""
    while True:
        try:
            keep = input(f"Do you want to keep the previous result ({result}) ? ").strip().lower()
            if keep == "y" or keep == "yes":
                num1 = result
                return num1
            elif keep == "n" or keep == "no":
                return None
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def is_valid_operator(op: str) -> bool:
    """return string with custom validation"""
    return op.strip() in ["+","-","*","/"]

def main() -> None:
    """main function of the calculator"""
    num1 = None
    continue_calc = True
    while continue_calc == True:
        if not num1:
            num1 = get_input("Enter a number : ",float)
        operator = get_input("Enter an operator (+, -, *, /): ",validation_func=is_valid_operator)
        num2 = get_input("Enter a number : ",float)
        result = calculus(num1,num2,operator)
        continue_calc = continue_calculating()
        if result != None:
            num1 = keep_result(num1,result)
        else:
            num1 = None

if __name__ == "__main__":
    main()
    