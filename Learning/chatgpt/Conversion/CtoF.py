def get_temperature_in_c() -> float:
    """prompt user for temperature in Celsius, validate and return it"""
    while True:
        try:
    
            celsius = float(input("input temperature in celsius :"))
            return celsius
        except ValueError:
            print("wrong value, input temperature in celsius :")

def celsius_to_fahrenheit(celsius :float) -> float:
    """Convert celsius to fahrenheit"""
    return round(celsius * 9 / 5 + 32, 1)

def main() -> None:
    """main function"""
    celsius = get_temperature_in_c()
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")

    a = "2"
    print(int(a)==a)
if __name__ == "__main__":
    main()