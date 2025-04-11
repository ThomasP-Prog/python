"""You are given a list of tuples, where each tuple represents a (product_id, price).
   You are also given a second list of tuples representing (product_id, quantity_sold).
   Create a dictionary where keys are the product_ids and values are the total revenue (price * quantity_sold) for that product.
   Assume each product_id appears exactly once in both lists."""

def total_revenue(id_price : list[tuple[int,int]], id_sold : list[tuple[int,int]]) -> dict:
    """Calculate total revenue in a dict"""
    if not id_price or not id_sold:
        return {}

    # Make a dict out if the list of tuple
    price_dict = dict(id_price)

    revenue_dict = {
        id : sold*price_dict[id] for id, sold in id_sold if id in price_dict
    }
    
    return revenue_dict

def print_revenue(revenue : dict) -> None:
    """Format revenue"""
    if not revenue:
        return
    
    # Width formatting
    id_lenght = max(len(str(id)) for id in revenue)
    # Add padding
    id_lenght += 1
    
    print(f"{'ID':<{id_lenght}} Total revenue ")
    for id, total in revenue.items():
        print(f"{id:<{id_lenght}} {total}")

def main() -> None:
    """main function"""
    id_price = [(0,10),(1,15),(2,50),(10,10)]
    id_sold = [(0,3),(1,5),(2,4),(10,5)]

    revenue = total_revenue(id_price,id_sold)
    print_revenue(revenue)

if __name__ == "__main__":
    main()

