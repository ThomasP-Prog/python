"""Write a function calculate_total_prices that takes a dictionary as input. 
   The keys of the dictionary are product IDs (strings), and the values are dictionaries containing product details 
   (e.g., {"name": "Laptop", "price": 1200, "quantity": 5}). The function should calculate and 
   print the total price of all products (price * quantity for each product)."""



def main() -> None:

    product_data = {
    "P1": {"name": "Laptop", "price": 1200, "quantity": 5},
    "P2": {"name": "Keyboard", "price": 75, "quantity": 10},
    "P3": {"name": "Mouse", "price": 25, "quantity": 20}
    }
# Expected output (printed):
# Total price: 8500


if __name__ == "__main__":
    main()