def get_temp(conversion :str) -> int|float:
    """Prompt user to enter an input and validate type"""
    while True:
        try:
            temp = float(input("Enter a temperature : ").strip())
            if conversion == "F":
                if temp <= -273.15:
                    print("Error. Temperature under limit (-459.69°F, absolute zero)")
                elif temp >= 5526:
                    print("Error. Temperature above limit (9980°F, temperature of the sun)")
                else:
                    return temp
            elif conversion == "C":
                if temp <= -459.67:
                    print("Error. Temperature under limit (-273.15°C, absolute zero)")
                elif temp >=  9980:
                    print("Error. Temperature above limit (5526°C, temperature of the sun)")
                else:
                    return temp   
            
        except ValueError:
                print("Error. The temperature as to be a number.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye")
            exit()

def get_type() -> str:
    """Ask user which convert they want"""
    while True:
        try:
            temp_type = input("Enter C to convert from Fahrenheit to Celsius or F to convert from Celsius to Fahrenheit : ").capitalize()
            if temp_type == 'F' or temp_type == 'C':
                return temp_type
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter C or F")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye")
            exit()

def continue_temp() -> bool:
    """Ask user if they want to continue converting"""
    while True:
        try:
            choice = input("do you want to enter another entry ? (yes/no) : ").strip().lower()
            if choice == 'y' or choice == 'yes':
                return True
            elif choice == 'n' or choice == 'no':
                return False
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter yes or no.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def temp_calc(temp :int|float, temp_type : str) -> None:
    """Print the conversion with realistic limit"""
    if temp_type == "F":
        calc = (temp * 9 / 5) + 32
        if calc <= -459.67:
            print("Error. Temperature under limit (-459.69°F, absolute zero)")
        elif calc >= 9980:
            print("Error. Temperature above limit (9980°F, temperature of the sun)")
        else:
            print(f"{temp}°C = {round(calc,2)}°F")
    if temp_type == "C":
        calc = (temp - 32 ) * 5 / 9
        if calc <= -273.15:
            print("Error. Temperature under limit (-273.15°C, absolute zero)")
        elif calc >= 5526 :
            print("Error. Temperature above limit (5526°C, temperature of the sun)")
        else:
            print(f"{temp}°F = {round(calc,2)}°C")

def main() -> None:
    """main function"""
    tbool = True
    while tbool:
        conversion = get_type()
        temp = get_temp(conversion)
        temp_calc(temp,conversion)
        tbool = continue_temp()

if __name__ == "__main__":
    main()