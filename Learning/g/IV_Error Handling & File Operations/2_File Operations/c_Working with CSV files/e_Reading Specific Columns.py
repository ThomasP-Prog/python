"""
Assume a CSV file products.csv exists with columns ProductID, ProductName, Price, Category. 
Write a function get_product_names_prices(filename: str) -> dict[str, float] that reads the file using csv.DictReader. 
Return a dictionary where keys are product names and values are their prices (converted to float). 
Handle potential FileNotFoundError and ValueError during float conversion (skip rows with invalid prices, maybe print a warning).

Expected Output (Dictionary): {'Laptop': 1200.50, 'Keyboard': 75.00, 'Coffee Mug': 15.99} (Warning printed for P104)
"""

import csv
from typing import Dict
from pathlib import Path

def get_product_names_prices(filename: str) -> Dict[str, float]:
    """
    Read products.csv  and returns a dict with name as key and price as value

    Args:
        filename : str

    Returns
        Dict[str,float]
    """
    script_directory = Path(__file__).parent
    full_path = script_directory / filename
    output_dict = {}
    try:
        print(f"--- Attempting to read {filename} ---")
        with open(full_path,mode="r",encoding="utf-8",newline='') as infile:
            reader = csv.DictReader(infile)
            try:
                for row_dict in reader:
                    product = row_dict.get('ProductID','None')
                    name = row_dict.get('ProductName','None')
                    price = float(row_dict.get('Price','None'))
                    output_dict[name] = price
                
            except ValueError:
                print(f"Warning, {product} price is not a float : {row_dict.get('Price','None')}")
        print(f"--- Reading successful ---")
    except FileNotFoundError:
        print(f"Error, file not found {full_path}")

    return output_dict

def main() -> None:
    """main function"""
    filename = "products.csv"
    prod_dict = get_product_names_prices(filename)
    print(prod_dict)

if __name__ == "__main__":
    main()