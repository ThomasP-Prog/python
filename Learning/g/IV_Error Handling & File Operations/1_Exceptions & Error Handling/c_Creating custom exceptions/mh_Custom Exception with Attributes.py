"""
- Define a custom exception InventoryError(Exception) that accepts item_id and message in its __init__ method and stores them as attributes.
- Define two subclasses: ItemNotFoundError(InventoryError) and OutOfStockError(InventoryError). OutOfStockError should also accept and 
store the available_stock in its __init__.
 -Simulate an inventory dictionary: inventory = {"item1": 5, "item2": 0, "item3": 10}.
 -Write a function request_item(item_id: str, quantity: int, current_inventory: dict) that:
    - Raises ItemNotFoundError(item_id, "Item not in inventory") if the item_id is not a key in current_inventory.
    - Raises OutOfStockError(item_id, "Item out of stock", available_stock=0) if the stock for the item is 0.
    - Raises OutOfStockError(item_id, f"Only {stock} available", available_stock=stock) if quantity is greater than the available stock.
    - If successful, print "Item request successful."

- Write calling code that uses try...except blocks to specifically catch ItemNotFoundError and OutOfStockError. 
When catching OutOfStockError, access its item_id and available_stock attributes to print a detailed message. 
Also include a general except InventoryError to catch any other potential inventory issues (though none are raised here).
- Sample Data: Use the sample inventory. Test requesting ("item1", 3), ("item2", 1), ("item1", 15), ("item4", 1)
"""

class InventoryError(Exception):
    
    def __init__(self, item_id: str, message: str = "Inventory error occurred"):
        self.item_id = item_id  # Store the custom attribute
        # Format a message for the parent Exception's __init__
        full_message = f"{message} (Item ID: {self.item_id})" 
        super().__init__(full_message)

class ItemNotFoundError(InventoryError):
    """Raised if item not in inventory"""
    pass


class OutOfStockError(InventoryError):
    """Raised if insufficient stock"""
    def __init__(self, item_id: str, message: str, available_stock: int):
        # Call the PARENT (InventoryError) __init__ first
        super().__init__(item_id, message) 
        # Store the additional attribute specific to this error
        self.available_stock = available_stock 

def request_item(item_id: str, quantity: int, current_inventory: dict) -> None:
    """
    Request if item is available or raise exception

    Args:
        item_id: str
        quantity: int
        current_inventory: dict

    Returns:
        None
    """
    if item_id not in current_inventory:
            raise ItemNotFoundError(item_id, "Item not in inventory")

    available_stock = current_inventory[item_id]

    if available_stock <= 0:
        raise OutOfStockError(item_id, "Item out of stock", available_stock=0) # Pass available_stock=0

    # 4. Check if requested quantity exceeds available stock
    if quantity > available_stock:
        raise OutOfStockError(item_id, f"Insufficient stock. Only {available_stock} available", available_stock=available_stock)


    print("Item request successful.")

def main() -> None:
    """main function"""
    test_list = [("item1", 3), ("item2", 1), ("item1", 15), ("item4", 1)]
    inventory = {"item1": 5, "item2": 0, "item3": 10}

    for test in test_list:
        try:
            request_item(test[0], test[1], inventory)
        except ItemNotFoundError as e: # Catch specific subclass FIRST
            print(f"Item Not Found Error: {e}. Item ID: {e.item_id}")
        except OutOfStockError as e: # Catch specific subclass SECOND
            print(f"Out Of Stock Error: {e}. Item ID: {e.item_id}, Available: {e.available_stock}")
        except InventoryError as e: # Catch parent class LAST (for any other InventoryErrors)
            print(f"General Inventory Error: {e}. Item ID: {e.item_id}")
        except Exception as e: # Optional: Catch any other totally unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()