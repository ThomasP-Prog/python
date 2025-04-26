"""You have a list representing stock data:
   stock_quotes = [("AAPL", 175.20, 176.50), ("GOOG", 2800.50, 2810.00), ("MSFT", 300.00, 301.80)],
   where each tuple is (Ticker, OpeningPrice, ClosingPrice).
   Use a loop and tuple unpacking to calculate the change in price for each stock (ClosingPrice - OpeningPrice)
   and store the results in a dictionary where the Ticker is the key and the price change is the value."""

def calculate_stock_changes(stock_quotes : list[tuple[str, float, float]]) -> dict[str, float]:
    """Substract closing_price and opening price and return result as dict"""
    if not stock_quotes:
        return {}
    stock_change = {}
    # Unpack stock_quotes
    for ticker, opening_price, closing_price in stock_quotes:
        # Calculate difference
        stock_change[ticker] = round(closing_price - opening_price,2)
    return stock_change

def print_stock_changes(changes: dict[str, float]) -> None:
    """Formats and prints the stock price changes."""
    if not changes:
        print("No stock change data to print.")
        return

    print(f"{'Ticker':<6} Change") # Adjust padding as needed
    print("-" * 15)
    for ticker, change in changes.items():
        # Optional: Add a '+' sign for positive changes
        print(f"{ticker:<6} {change:+.2f}") 

def main() -> None:
    """main function"""
    stock_quotes = [("AAPL", 175.20, 176.50), ("GOOG", 2800.50, 2810.00), ("MSFT", 300.00, 301.80)]
    stock_change = calculate_stock_changes(stock_quotes)
    print_stock_changes(stock_change)


if __name__ == "__main__":
    main()