def get_input(prompt : str, data_type : type = str) -> str|int|float:
    """Prompt user to enter a value and validate type"""
    while True:
        try:
            new_input = input(prompt)

            if data_type in [float,int]:
                if new_input.replace('.', '', 1).isdigit() or (new_input.startswith('-') and new_input[1:].replace('.', '', 1).isdigit()):
                    return int(new_input) if '.' not in new_input else float(new_input)
            else:
                return new_input
        except ValueError:
            if data_type == int:
                print("Error. Enter a whole number.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def add_single(elements : list) -> None:
    """Prompt user to enter a new element"""
    elements.append(get_input("Add an element to the list : "))

def add_with_index(elements : list) -> None:
    """Prompt user to enter a new element with an index"""
    while True:
        print(f"range of index : 0 to {len(elements)}")
        index = get_input("Enter the index of the new value : ",int)
        if 0 <= index <= len(elements):
            break
        print(f"Invalid index. Please enter a value between 0 and {len(elements)}.")
    new_element = get_input("Add an element to the list : ")
    elements.insert(index,new_element)

def remove_element(elements : list) -> None:
    """Prompt user to remvoe an element"""
    if not elements:
        print("Error: The list is empty. No elements to remove.")
        return
    
    print(f"Current elements : {elements}")
    while True:
        deleted_element = get_input("Enter the element you want to remove : ")
        if deleted_element in elements:
            elements.remove(deleted_element)
            break
        print("Error. Element not in the list")
        


def main() -> None:
    elements = []
    for _ in range(5):
        add_single(elements)
    add_with_index(elements)
    remove_element(elements)
    remove_element(elements)
    print(f"Updated list: {elements}")

if __name__ == "__main__":
    main()