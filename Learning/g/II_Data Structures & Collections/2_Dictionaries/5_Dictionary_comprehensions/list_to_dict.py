"""Given a list of strings fruits = ['apple', 'banana', 'cherry'],
   create a dictionary where the keys are the fruits and the values
   are the number of vowels in each fruit name."""

def dict_vowels(fruits : list[str]) -> dict[str,int]:
    """Transform list of strings into a dict with fruit as keys and number of vowels as values"""
    fruit_dict = {}
    if fruits:
        VOWELS = "aeiou"
        fruit_dict = {
            fruit : sum(1 for char in fruit.lower() if char in VOWELS) for fruit in fruits
        }
    return fruit_dict

def print_dict(fruits : dict[str,int]) -> None:
    """Formatting dict"""
    if fruits:
        print(f"{'Fruits':<9} {'Vowels'}")
        for fruit in fruits:
            vowels = fruits[fruit]
            print(f"{fruit:<11} {vowels}")

    else:
        print("Error. No dict entered")


def main() -> None:
    """main function"""
    fruits = ['apple', 'banana', 'cherry']
    fruit_dict = dict_vowels(fruits)
    print_dict(fruit_dict)

if __name__ == "__main__":
    main()