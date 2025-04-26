"""Task: Write a function find_cheapest_in_category that takes two arguments:
   - A list of tuples, where each tuple represents a product (product_name: str, price: float, category: str).
   - A string representing the category_to_find. The function should return the product_name (string) 
   of the cheapest product within the specified category_to_find. If no products are found in that category, it should return None."""

def find_cheapest_in_category(product_list : list[tuple[str,float,str]],category : str) -> str|None:
    """return the product_name of the cheapest product within the specified category"""
    if not product_list or not category:
        return None
    min_product = None
    min_price_so_far = float('inf')
    for product,price,cat in product_list:
        if cat == category:
            if price < min_price_so_far:
                min_price_so_far = price
                min_product = product
    return min_product

def print_cheapest(product : str|None, category : str) -> None:
    """Print cheapest product"""
    if not category:
        print("No category entered")
        return
    if not product:
        print(f"No product found in {category}")
        return
    print(f"{product} is the cheapest product in {category}")

def main() -> None:
    """main function"""
    products_list = [
    ("Laptop", 1200.00, "Electronics"),
    ("Keyboard", 75.00, "Electronics"),
    ("Mouse", 25.00, "Electronics"),
    ("Desk Chair", 150.00, "Furniture"),
    ("Notebook", 2.50, "Stationery"),
    ("Pen Set", 15.00, "Stationery"),
    ("Desk Lamp", 45.00, "Furniture"),
    ("Monitor", 300.00, "Electronics"),
]

    category = "Electronics"
    # Expected output for this data and category: "Mouse"

    category_not_found = "Groceries"
    # Expected output for this data and category: None

    cheapest_product = find_cheapest_in_category(products_list,category)
    print_cheapest(cheapest_product,category)
    cheapest_product = find_cheapest_in_category(products_list,category_not_found)
    print_cheapest(cheapest_product,category_not_found)


if __name__ == "__main__":
    main()