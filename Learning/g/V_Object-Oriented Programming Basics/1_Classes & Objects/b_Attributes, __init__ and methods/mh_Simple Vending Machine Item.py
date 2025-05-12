"""
Define a class VendingMachineItem.

    Its __init__ should take name (str), price (float), and quantity_in_stock (int).
    Add a method get_info() that returns a string like "Item: [Name], Price: $[Price], Stock: [Quantity]".
    Add a method purchase(num_items: int = 1) that:
        Checks if num_items is positive. If not, print "Invalid quantity." and do nothing.
        Checks if there's enough stock. If num_items requested is greater than quantity_in_stock, print "Out of stock for desired quantity." and do nothing.
        If valid and in stock, decrease quantity_in_stock by num_items and print "Purchased [num_items] of [Name].".

Sample Usage: Create an item, get its info, try to purchase a valid quantity, try to purchase too many, try to purchase an invalid quantity, get info again.
"""

class VendingMachineItem:
    def __init__(self, name:str, price:float, quantity_in_stock:int) -> None:
        """Initialize VendingMachineItem"""
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def get_info(self) -> str:
        """Returns the info of the item as str"""
        return f"Item : {self.name}, Price : {self.price}, Stock : {self.quantity_in_stock}"
    
    def purchase(self,num_item:int = 1) -> None:
        """Purchase the number of item if enough are available"""
        if num_item <= 0:
            print("Invalid quantity.")
        else:
            if self.quantity_in_stock >= num_item:
                self.quantity_in_stock -= num_item
                print(f"Purchased {num_item} of {self.name}")
            else:
                print("Out of stock for desired quantity")

def main() -> None:
    """main function"""
    new_item = VendingMachineItem("water",2.5,10)
    item_info = new_item.get_info()
    print(item_info)
    new_item.purchase(5)
    new_item.purchase(10)
    item_info = new_item.get_info()
    print(item_info)

if __name__ == "__main__":
    main()