"""Write a function calculate_order_total(items: List[Dict[str, Union[str, int, float]]], discount_code: Optional[str] = None) -> float.
    - The items parameter is a list of dictionaries, where each dictionary represents an item and has keys 'name' (str), 'price' (float), and 'quantity' (int).
    - The discount_code is an optional string.
    - The function should calculate the total cost (price * quantity for all items).
    - If a discount_code is provided and equals "SAVE10", apply a 10% discount to the total cost.
    - Return the final total cost as a float.
    - Include type hints for all parameters, the return value, and significant internal variables (like subtotal, total)."""

from typing import List,Dict,Union,Optional

def calculate_order_total(items: List[Dict[str, Union[str, int, float]]], discount_code: Optional[str] = None) -> float:
    """
    Calculate total and apply discount when needed

    Args:
        items : List[Dict[str, Union[str, int, float]]]
        discount_code : Optional[str] = None

    Returns:
        total : float
    """
    subtotal : float = 0.0
    total_cost : float = 0.0

    for item in items:
        price = item.get("price",0)
        quant = item.get("quantity",0)
        if price > 0 and quant > 0:
            subtotal += price*quant
    if discount_code and discount_code == "SAVE10":
        total_cost = subtotal * 0.9
    else:
        total_cost = subtotal
    return total_cost

def main() -> None:
    """main function"""
    order_items = [
        {'name': 'Laptop', 'price': 1200.00, 'quantity': 1},
        {'name': 'Mouse', 'price': 25.50, 'quantity': 2}
    ]

    # Example call 1:
    total1 = calculate_order_total(order_items) 
    print(total1)
    # Expected: 1200.00 * 1 + 25.50 * 2 = 1251.00
    # Example call 2:
    total2 = calculate_order_total(order_items, discount_code="SAVE10")
    print(total2)
    # Expected: 1251.00 * 0.9 = 1125.90
    # Example call 3:
    total3 = calculate_order_total(order_items, discount_code="INVALID")
    print(total3)
    # Expected: 1251.00 
    # Example call 4:
    total4 = calculate_order_total([])
    print(total4)
    # Expected: 0.0

if __name__ == "__main__":
    main()