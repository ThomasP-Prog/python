def calculated_numbers(numbers : list[int]) -> list[int]:
    if not numbers:
        return []
    try:
        return [number*number for number in numbers if number%3 == 0 and number%2 == 0]
    except TypeError:
        raise TypeError("Input must be a list of integers")

def main():
    number_list = [
        list(range(21)),
        list(range(0,50,2)),
        []
    ]
    for number in number_list:
        try:
            print(f"numbers :\n {','.join(map(str,number))}")
            square = calculated_numbers(number)
            print(f"square numbers divisible by 3 :\n {','.join(map(str,square))}")
        except TypeError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()