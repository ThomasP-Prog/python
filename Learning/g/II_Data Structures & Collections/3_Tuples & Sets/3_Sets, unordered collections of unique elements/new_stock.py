"""Take the function you wrote for the "Hard" tuple exercise
   (calculating stock price changes into a dictionary {'Ticker': change}).
   Modify it so that it now also returns a set containing the tickers of
   all stocks that had a positive price change (closing > opening)."""

def calculate_stock_changes(stock_quotes : list[tuple[str, float, float]]) -> tuple[dict[str, float], set[str]]:
    """Calculates stock changes and identifies tickers with positive changes."""
    if not stock_quotes:
        return {}, set()
    stock_change = {}
    positive_stock = set()
    # Unpack stock_quotes
    for ticker, opening_price, closing_price in stock_quotes:
        # Calculate difference
        change = round(closing_price - opening_price,2)
        stock_change[ticker] = change
        if change > 0:
            positive_stock.add(ticker)

    return stock_change,positive_stock

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

def print_positive_stock(positive_stock : set[str]) -> None:
    """Formats and prints positive tickers"""
    if not positive_stock:
        return
    print("Positive tickers :")
    for ticker in positive_stock:
        print(ticker)
    

def main() -> None:
    """main function"""
    stock_quotes = [("AAPL", 179.20, 176.50), ("GOOG", 2800.50, 2810.00), ("MSFT", 300.00, 301.80)]
    stock_change,positive_stock = calculate_stock_changes(stock_quotes)
    print_stock_changes(stock_change)
    print_positive_stock(positive_stock)


if __name__ == "__main__":
    main()