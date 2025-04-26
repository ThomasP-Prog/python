""" Create a tuple containing the names of the days of the week (strings).
    Access and print the first and last day.
    Try (and fail, observing the TypeError) to change the second day to something else."""

def main() -> None:
    """main function"""

    # Create tuple
    week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    print(week[0])
    print(week[-1])
    
    # Test to change immutable object
    try:
        week[1] = "Otherday" 
    except TypeError as e:
        print(f"Successfully caught expected error: {e}") 

if __name__ == "__main__":
    main()