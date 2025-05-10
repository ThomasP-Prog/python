"""
Assume a CSV file sales_records.csv with columns OrderID, ProductCategory, SaleAmount. 
Write a function summarize_sales_by_category(filename: str) -> dict[str, dict]. Read the file. 
Aggregate the sales to find the total SaleAmount and the NumberOfSales for each unique ProductCategory. 
Return a dictionary where keys are ProductCategory strings, and values are dictionaries like {'total_sales': float, 'number_of_sales': int}. 
Ensure SaleAmount is converted to float; skip rows with invalid SaleAmount (print a warning). Handle FileNotFoundError.
"""

import csv
from pathlib import Path

def summarize_sales_by_category(filename: str) -> dict[str, dict]:
    """
    Summarize sales from sales_records.csv

    Args:
        filename: str

    Returns:
        dict[str, dict]
    """
    file_directory = Path(__file__).parent
    full_path = file_directory  / filename

    sale_dict = {}

    try:
        print(f"--- Attempting to read file {filename} ---")
        with open(full_path, mode='r',encoding='utf-8',newline='') as infile:
            reader = csv.DictReader(infile)

            for row_dict in reader:
                try:
                    order = row_dict.get('OrderID','None')
                    category = row_dict.get('ProductCategory','None')
                    sale = row_dict.get('SaleAmount','None')
                    sale = float(sale)

                    if category not in sale_dict:
                        sale_dict[category] = {'total_sales': 0.0, 'number_of_sales': 0}

                    sale_dict[category]['total_sales'] += sale
                    sale_dict[category]['number_of_sales'] += 1
                except ValueError:
                    print(f"Warning, order '{order}' sale is invalid : '{sale}'")
        print(f"--- Finished to reading file {filename} ---")
    except FileNotFoundError as e:
        print(f"Error, {e}")
    return sale_dict

def main() -> None:
    """main function"""
    input_file = "sales_records.csv"
    sale_dict = summarize_sales_by_category(input_file)

    print(sale_dict)

if __name__ == "__main__":
    main()