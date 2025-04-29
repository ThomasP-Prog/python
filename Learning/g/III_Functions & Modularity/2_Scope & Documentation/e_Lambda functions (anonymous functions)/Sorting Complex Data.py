"""You have a list of tuples, where each tuple represents (item_name, price, quantity): 
   inventory = [('apple', 0.5, 10), ('banana', 0.3, 20), ('orange', 0.6, 15)]
   Use the sorted function and a lambda to sort the inventory list based on the total value of each item 
   (price * quantity), from highest value to lowest. """

def main() -> None:
    """main function"""

inventory = [('apple', 0.5, 10), ('banana', 0.3, 20), ('orange', 0.6, 15)]
sorted_inventory = sorted(inventory,
                          key=lambda item : item[1]*item[2],
                          reverse=True)
print(sorted_inventory)
# Expected: [('orange', 0.6, 15), ('banana', 0.3, 20), ('apple', 0.5, 10)]
# (Because orange=9.0, banana=6.0, apple=5.0)

if __name__ == "__main__":
    main()