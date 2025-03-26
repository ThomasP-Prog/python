from random import randrange

def get_numeric_input(prompt: str):
    """Prompts user for a numeric input and ensures correct type."""
    while True:
        try:
            user_input = input(prompt).strip()
            return float(user_input) if '.' in user_input else int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def remove_occurrence(numbers : list) -> list:
    """Prompt user to enter the occurrence they want to remove"""
    if not numbers:
        print("The list is empty.")
        return numbers
    
    print(f"Number list : {numbers}")
    occurence = get_numeric_input("Enter a number from the list to remove all occurrences: ")

    if occurence not in numbers:
        print(f"{occurence} is not in the list.")
        return numbers

    updated_list = [num for num in numbers if num != occurence]
    print(f"All occurrences of {occurence} have been removed.")
    return updated_list

def main() -> None:
    numbers = []
    for _ in range(10):
        numbers.append(randrange(6))
    numbers = remove_occurrence(numbers)
    print(f"Updated list : {numbers}")

if __name__ == "__main__":
    main()