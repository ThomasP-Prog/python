def get_temp() -> int|float:
    """prompt user to enter a temperature and validate"""
    while True:
        try:
            temp = float(input("Enter your temperature : "))
            if temp >= 30 and temp <= 45:
                return temp
            else:
                print("Temperature as to be between 30°C and 45°C")
        except ValueError:
            print("Error, you need to enter a number.")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()

def check_temp(temp :int|float) -> str:
    """evaluate condition based on temperature"""
    condition = "fever" if temp > 37.5 else ("Normal temperature" if temp >= 36 and temp <= 37.5 else "Low temperature")
    return condition

def main() -> None:
    """main funciton"""
    temp = get_temp()
    condition = check_temp(temp)
    print(f"Temperature is {temp}°C. {'you have '+ condition if condition == 'fever' else condition}")

if __name__ == "__main__":
    main()