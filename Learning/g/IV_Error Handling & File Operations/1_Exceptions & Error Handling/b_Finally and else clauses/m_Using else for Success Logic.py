"""
Write a function get_and_process_value(data_dict: dict, key: str) that tries to get a value from data_dict using key.

    try: Attempt value = data_dict[key].
    except KeyError: Print "Error: Key '[key]' not found."
    else: If the key was found, check if the value is an integer (isinstance(value, int)). 
    If it is, print "Processing integer: [value*2]". If it's not an integer, print "Value found but not an integer: [value]".
    finally: Print "Finished attempting to process key: [key]"
"""

def get_and_process_value(data_dict: dict, key: str) -> None:
    """
    Tries to get the value of data[key] and print accordingly

    Args:
        data_dict: dict
        key: str

    Returns:
        print
    """
    try:
        value = data_dict[key]
    except KeyError:
        print(f"Error: Key '{key}' not found.")
    else:
        if isinstance(value,int):
            print(f"Processing integer: {value*2}")
        else:
            print(f"Value found but not an integer: {value}")
    finally:
        print(f"Finished attempting to process key: {key}")


def main() -> None:
    """main function"""

    my_data = {"id": 101, "score": 85, "name": "Alice", "attempts": [1, 2]}
    get_and_process_value(my_data, "score") 
    # Expected: Prints "Processing integer: 170", then "Finished..."
    get_and_process_value(my_data, "name") 
    # Expected: Prints "Value found but not an integer: Alice", then "Finished..."
    get_and_process_value(my_data, "age") 
    # Expected: Prints "Error: Key 'age' not found.", then "Finished..."

if __name__ == "__main__":
    main()