"""Write a complete docstring for the following function according to standard Python conventions (like PEP 257), including:
   - A short summary line,
   - Descriptions for arguments and return value."""

def check_temperature_status(temp_celsius : int) -> str:
    """
    return status if water depending on the given temperature

    Args:
        temp_celsius : current temperature in Celsius

    Returns:
        string of the current status of water
    """
    # Conversion constants
    FREEZING_POINT_C = 0.0
    BOILING_POINT_C = 100.0

    if temp_celsius < FREEZING_POINT_C:
        return "Freezing"
    elif temp_celsius >= BOILING_POINT_C:
        return "Boiling"
    else:
        return "Normal"
    
def main() -> None:
    """main function"""
    temp_celsius = -5
    print(check_temperature_status(temp_celsius))
    temp_celsius = 25
    print(check_temperature_status(temp_celsius))
    temp_celsius = 100
    print(check_temperature_status(temp_celsius))

if __name__ == "__main__":
    main()