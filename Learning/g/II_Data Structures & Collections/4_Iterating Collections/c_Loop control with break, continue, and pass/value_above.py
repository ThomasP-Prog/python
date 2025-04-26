"""Write a function find_first_value_above_threshold(data: list[float], threshold: float) -> float | None. 
   The function should iterate through the data list. Use a for loop and break to return the first value 
   it encounters that is strictly greater than the threshold. If no such value is found after checking the entire list, return None"""

def find_first_value_above_threshold(data: list[float], threshold: float) -> float | None:
    """Return first value above threshold or None if no value found"""
    if not data or threshold is None:
        return None
    
    value_above_threshold = None
    for number in data:
        if number > threshold:
            value_above_threshold = number
            break

    return value_above_threshold

def print_threshold_result(value : float, threshold : float) -> None:
    """Print the value above threshold"""
    if threshold is None:
        return
    elif not value:
        print(f"No value above {threshold} found")
    else:
        print(f"First value above threshold {threshold} is {value}")

def main() -> None:
    """main function"""

    numbers1 = [10.5, 2.3, 15.0, 9.9, 20.1, 5.5]
    limit1 = 12.0
    value1 = find_first_value_above_threshold(numbers1,limit1)
    print_threshold_result(value1,limit1)
    # Expected output: 15.0

    numbers2 = [1, 5, 3, 7, 2]
    limit2 = 8.0
    value2 = find_first_value_above_threshold(numbers2,limit2)
    print_threshold_result(value2,limit2)
    # Expected output: None

if __name__ == "__main__":
    main()