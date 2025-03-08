def print_price_list(products : list[tuple[str, float]]) -> None:
    """Prints a neatly aligned price list of products"""
    if not products:
        print("List empty")
        return
    print("PRICE LIST".center(30, "="))
    for name,price in products:
        print(f"{name:<15} : ${price:>5.2f}")
    
def main() -> None:
    products = [("Tomato",2),("Banana",3),("Apple",5)]
    print_price_list(products)

if __name__ == "__main__":
    main()

    