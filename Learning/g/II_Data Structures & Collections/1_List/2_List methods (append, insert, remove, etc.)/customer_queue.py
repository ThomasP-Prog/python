def get_string_input(prompt: str) -> str:
    """Prompt user for a valid name input (no numbers or special characters except hyphens)."""
    while True:
        try:
            new_input = input(prompt).strip()
            if not new_input:
                print("Customer name can't be empty.")
                continue
            if not new_input.replace("'", "").replace("-", "").isalpha():
                raise ValueError
            return new_input.title()
        except ValueError:
            print("Names cannot contain numbers or special characters (except hyphens).")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def get_int_input(prompt: str, min_val: int = 0, max_val: int = None) -> int:
    """Prompt user for a valid integer input within a specified range."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Error: Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Error. Enter a valid integer.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def add_customer(customers: list) -> None:
    """Add a new customer to the queue."""
    new_customer = get_string_input("Enter new customer name: ")
    customers.append(new_customer)
    print(f"{new_customer} added to the queue.")

def add_priority_customer(customers: list) -> None:
    """Insert a customer at a priority position in the queue."""
    if not customers:
        print("No customers in the queue. Adding normally.")
        add_customer(customers)
        return

    print(f"Current Queue: {', '.join(customers)}")
    index = get_int_input(f"Enter priority index (0 to {len(customers)}): ", 0, len(customers))
    new_customer = get_string_input("Enter new customer name: ")
    customers.insert(index, new_customer)
    print(f"{new_customer} added at position {index}.")

def remove_customer(customers: list) -> None:
    """Remove the first customer in the queue (FIFO order)."""
    if not customers:
        print("No customers in queue to remove.")
        return
    print(f"{customers.pop(0)} has been served and removed from the queue.")

def main() -> None:
    customers = []
    for _ in range(5):
        add_customer(customers)
    
    add_priority_customer(customers)

    while customers:
        print(f"\nCurrent Queue: {', '.join(customers)}")
        remove_customer(customers)

    print("The queue is now empty.")

if __name__ == "__main__":
    main()