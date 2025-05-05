"""
- Define a custom exception ValueTooLowError that inherits from ValueError.
- Write a function check_temperature(temp_celsius: float) that raises ValueTooLowError with an 
informative message if temp_celsius is below absolute zero (-273.15 C).
- Otherwise, it should print "Temperature is valid."
- Write code that calls this function with a valid temperature (e.g., 20) and an invalid temperature (e.g., -300) 
inside separate try...except ValueTooLowError blocks, printing the exception message if caught.
- Test with check_temperature(20), check_temperature(-300)
"""
class ValueTooLowError(ValueError):
    """
    Raised when temp is under absolute zero
    """
    pass

def check_temperature(temp_celsius: float) -> None:
    """
    Print if temp is valid or raise ValueTooLowError

    Args:
        temp_celsius : float

    Returns
        None     
    """
    if temp_celsius < -273.15:
        raise ValueTooLowError(f"{temp_celsius} under absolut zero.")
    else:
        print("Temperature is valid")

def main() -> None:
    """main function"""
    temp_to_check = [20,-300]
    for temp in temp_to_check:
        try:
            check_temperature(temp)
        except ValueTooLowError as e:
            print(f"Error, {e}")

if __name__ == "__main__":
    main()
        