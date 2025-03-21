def continue_calculating() -> bool|None:
    """Prompt user to enter y/n to continue calculating"""
    while True:
        try:
            next_op = input("Do you want to continue calculating ? y/n ").strip().lower()
            if next_op == "y":
                return True
            elif next_op == "n":
                print("You exited the program. Goodbye.")
                exit()
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()

def keep_result(num1 :int|float,result :int|float) ->int|float|None:
    """Prompt user to enter y/n to keep previous result"""
    while True:
        try:
            keep = input(f"Do you want to keep the previous result ({result}) ? y/n ").strip().lower()
            if keep == "y":
                num1 = result
                return num1
            elif keep == "n":
                return None
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()
