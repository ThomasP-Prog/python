"""Write a function check_unique_items_in_orders(orders: list[dict]) -> tuple[list[str], list[str]]. 
   The input is a list of order dictionaries, where each dictionary has an 'order_id' (str) and 
   'items' (list of item strings). The function should validate the orders based on two criteria:
   - Each order must have a non-empty 'items' list.
   - Within each order, all item strings must be unique (no duplicate items in a single order's 'items' list). 
   Iterate through the orders. Use continue to skip to the next order if it fails validation rule #1. 
   Use a nested loop (or a set conversion) to check rule #2; if rule #2 fails, add the order_id to a list of invalid_order_ids 
   and use continue (or break from the inner check if appropriate) to move to the next order. If an order passes both checks, 
   add its order_id to a list of valid_order_ids. Use pass if needed as a placeholder. Return a tuple: (valid_order_ids, invalid_order_ids)."""

def check_unique_items_in_orders(orders: list[dict]) -> tuple[list[str], list[str]]:
    """return valid and invalid order_id"""
    if not orders:
        return ([], [])
    valid_list = []
    invalid_list = []

    for order in orders:
        items = order.get("items","")
        item_set = set()
        if items == None or not items:
            invalid_list.append(order.get("order_id","missing id"))
            continue
        if len(set(items)) != len(items):
            invalid_list.append(order.get("order_id","missing id"))
            continue
        valid_list.append(order.get("order_id","missing id"))
    return (valid_list,invalid_list)

def print_list(sorted_ids : tuple[list[str], list[str]]) -> None:
    """print the list"""
    if not sorted_ids:
        return
    print(f"Valid order_ids : {','.join(map(str,sorted_ids[0]))}")
    print(f"Invalid order ids : {','.join(map(str,sorted_ids[1]))}")


def main() -> None:
    """main function"""
    orders_data = [
        {'order_id': 'ORD101', 'items': ['apple', 'banana', 'apple']}, # Duplicate item
        {'order_id': 'ORD102', 'items': ['orange', 'grape']},        # Valid
        {'order_id': 'ORD103', 'items': []},                         # Empty items list
        {'order_id': 'ORD104', 'items': ['milk', 'bread', 'eggs']},   # Valid
        {'order_id': 'ORD105', 'items': ['coffee', 'sugar', 'coffee']} # Duplicate item
    ]
    # Expected output: (['ORD102', 'ORD104'], ['ORD101', 'ORD103', 'ORD105']) 
    # (Order within lists doesn't matter)

    sorted_ids = check_unique_items_in_orders(orders_data)

    print_list(sorted_ids)

if __name__ == "__main__":
    main()