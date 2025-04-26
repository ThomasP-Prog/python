"""Write a function that accepts a list of numbers and returns a tuple containing two elements:
   the count of even numbers and the count of odd numbers in the list."""

def count_even_odd_numbers(numbers : list[int]) -> tuple[int,int]:
    if not numbers:
        return 0,0

    even = 0
    odd = 0
    for number in numbers:
        if number%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

def main() -> None:
    numbers = list(range(0,20))
    even_odd_numbers = count_even_odd_numbers(numbers)

    print(f"Numbers list : {numbers}")
    print(f"Number of even numbers : {even_odd_numbers[0]}")
    print(f"Number of odd numbers : {even_odd_numbers[1]}")

if __name__ == "__main__":
    main()