"""Given a dictionary prices = {'apple': 0.5, 'banana': 0.25, 'orange': 0.6, ' Grapes ': 2.5},
   create a new dictionary containing only the fruits with prices less than $1.00.
   The keys in the new dictionary should be the fruit names, standardized to lowercase
   and with leading/trailing whitespace removed, and the values should be the original prices."""

def low_prices(prices : dict[str,float]) -> dict[str,float]:
    if prices:
        low_prices_dict = {
            fruit.lower().strip() : price
            for fruit, price in prices.items()
            if price < 1.0
        }
        return low_prices_dict
    else:
        return {}
    
def print_dict(low_prices : dict[str,float]):
    if low_prices:
        print("Fruits with price lower then 1€ : ")
        print(f"{'Fruit':<9} Price")
        for fruit, price in low_prices.items():
            print(f"{fruit:<10} {price}")

    
def main() -> None:
    prices = {'apple': 0.5, 'banana': 0.25, 'orange ': 0.6, ' Grapes ': 2.5}
    low_prices_dict = low_prices(prices)
    print_dict(low_prices_dict)

if __name__ == "__main__":
    main()