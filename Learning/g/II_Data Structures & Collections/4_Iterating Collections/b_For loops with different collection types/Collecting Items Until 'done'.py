"""Write a program that asks the user to enter items for a shopping list. Use a while loop to keep asking for items. 
   Each item entered should be added to a list. The loop should stop when the user enters the word "done" (case-insensitive). 
   After the loop finishes, print the final shopping list."""

def create_shopping_list() -> None:
    """Ask user to enter items in the list until they say 'done'"""
    item = ""
    end_loop = "done"
    shopping_list = []

    while item.lower() != end_loop:
        try:
            item = input("Enter an item (or 'done' to finish): ").strip()
            if item.isalpha():
                if item != end_loop:
                    shopping_list.append(item.lower())
            else:
                raise ValueError

        except ValueError:
            print("Item has to be a word")
    print(f"Your shopping list : {shopping_list}")

def main() -> None:
    """main function"""
    create_shopping_list()

if __name__ == "__main__":
    main()