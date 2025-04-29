"""Take your solution code for the exercise find_cheapest_in_category (from the previous section on iteration). 
   Add appropriate type hints to the function signature (parameters and return value) and annotate the key variables 
   within the function (like min_product_name and min_price_so_far). Use Optional if needed for the return type."""

from typing import List,Tuple,Optional

def find_cheapest_in_category(product_list : List[Tuple[str,float,str]],category : str) -> Optional[str]:
    """
    find the product_name of the cheapest product within the specified category
    
    Args:
        product_list : List[Tuple[str,float,str]]
        category : string

    Returns:
        name of category as a string or None
    
    """
    if not product_list or not category:
        return None
    min_product : str = None
    min_price_so_far : float = float('inf')
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

    cheapest_item : str|None = find_cheapest_in_category(products_list,category)
    print_cheapest(cheapest_item,category)

if __name__ == "__main__":
    main()