"""Create a nested dictionary to represent a simple inventory system
   for a small store with different departments (electronics, clothing, groceries).
   Each department should have at least 3 items with properties like name, price, and quantity.
   Write code to display the total value of inventory in each department"""

def get_departement() -> str:
    while True:
        try:
            print("Enter which departement total value you want :")
            departement = input("Possible value : 'electronics', 'clothing', 'groceries' or 'all' : ").strip()
            if departement == 'electronics' or departement == 'clothing' or departement == 'groceries' or departement == "all":
                return departement
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter 'electronics', 'clothing', 'groceries' or 'all'")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye")
            exit()

def departement_value(inventory : dict) -> None:
    if not inventory:
        print("No inventory")
        return
    else:
        value = 0
        departement = get_departement()

        print(f"\n--- {departement.upper()} INVENTORY REPORT ---")
        print(f"{'Item':<15} {'Price':<10} {'Quantity':<10} {'Value':<10}")
        print("-" * 45)

        departments_to_calculate = [departement] if departement != 'all' else inventory.keys()
    
        for dept in departments_to_calculate:
            if dept in inventory:
                items = inventory[dept]
                for item_id in items:
                    price = items[item_id].get('price', 0)
                    quantity = items[item_id].get('quantity', 0)
                    value += price * quantity
                    print(f"{item_id:<15} €{price:<9} {quantity:<10} {value} €")
        print("-" * 45)
        print(f"Total value: {value}€")

def main() -> None:
    inventory = {
        'electronics' : {
            'pc' : {'price' : 2000, 'quantity' : 10},
            'screen' : {'price' : 300, 'quantity' : 5},
            'keyboard' : {'price' : 200, 'quantity' : 4},
            },
        'clothing' : {
            't-shirt' : {'price' : 50, 'quantity' : 12},
            'shoes' : {'price' : 300, 'quantity' : 4},
            'jean' : {'price' : 70, 'quantity' : 6},
            },
        'groceries' : {
            'apple' : {'price' : 8, 'quantity' : 15},
            'banana' : {'price' : 6, 'quantity' : 25},
            'cheese' : {'price' : 10, 'quantity' : 9},
            }
        }
    departement_value(inventory)

if __name__ == "__main__":
    main()