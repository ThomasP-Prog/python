"""Write a function calculate_total_prices that takes a dictionary as input. 
   The keys of the dictionary are product IDs (strings), and the values are dictionaries containing product details 
   (e.g., {"name": "Laptop", "price": 1200, "quantity": 5}). The function should calculate and 
   print the total price of all products (price * quantity for each product)."""

def calculate_total_prices(product_data : dict) -> None:
    """Calculate total product value"""
    if not product_data:
        print("No data entered")
        return
    
    total_value = 0.0

    for product_id,data in product_data.items():

        if not isinstance(data, dict):
            print(f"Warning: Skipping product '{product_id}' - data is not a dictionary: {data}")
            continue

        price = data.get("price",0)
        quant = data.get("quantity",0)

        if not isinstance(price,int|float):
            print(f"Warning: Skipping product '{product_id}' - invalid price type: {price}")
            continue
        if not isinstance(quant,int):
            print(f"Warning: Skipping product '{product_id}' - invalid price type: {quant}")
            continue

        total_value += price*quant
    print(f"Total price : {total_value}")

def main() -> None:
    """main function"""
    product_data = {
    "P1": {"name": "Laptop", "price": 1200, "quantity": 5},
    "P2": {"name": "Keyboard", "price": 75, "quantity": 10},
    "P3": {"name": "Mouse", "price": 25, "quantity": 20}
    }
    product_data_mixed = {
        "P1": {"name": "Laptop", "price": 1200, "quantity": 5},
        "P2": {"name": "Keyboard", "price": 75}, # Missing quantity
        "P3": {"name": "Mouse", "price": "25", "quantity": 20}, # Price as string
        "P4": {"name": "Monitor", "quantity": 2}, # Missing price
        "P5": None, # Invalid data type
        "P6": {"name": "Webcam", "price": 50, "quantity": 10}
    }

    calculate_total_prices(product_data)
    calculate_total_prices(product_data_mixed)

if __name__ == "__main__":
    main()