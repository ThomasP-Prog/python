"""
Write a function add_price_category(input_filename: str, output_filename: str). 
Assume input_filename points to a CSV with columns Item, Price. Read the data using csv.DictReader. 
Based on the Price (convert to float, handle ValueError), add a new 'Category' column:
    - Price < 10: Category = "Inexpensive"
    - 10 <= Price < 100: Category = "Moderate"
    - Price >= 100: Category = "Expensive"
    - If price conversion fails, Category = "Unknown" Write the original data plus the new 'Category' 
    column to output_filename using csv.DictWriter. Ensure the output has headers: Item, Price, Category. 
    Handle FileNotFoundError for the input.
"""

import csv
from pathlib import Path

def add_price_category(input_filename: str, output_filename: str) -> None:
    """
    Take items.csv and make a new file items_output.csv adding the price category

    Args:
        input_filename: str
        output_filename: str
    
    Returns:
        None
    """
    file_directory = Path(__file__).parent
    input_path = file_directory / input_filename
    output_path = file_directory / output_filename

    try:
        print(f"--- Attempting to process {input_filename} and {output_filename} ---")
        with open(input_path,mode='r',encoding='utf-8',newline='') as infile ,\
            open(output_path,mode='w',encoding='utf-8',newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['Item','Price','Category']
            writer = csv.DictWriter(outfile,fieldnames=fieldnames)
            writer.writeheader()

            for rowdict in reader:
                try:
                    price = rowdict.get('Price','None')
                    price = float(price)
                    if price < 10:
                        category = "Inexpensive"
                    elif 10 <= price < 100:
                        category = "Moderate"
                    else:
                        category = "Expensive"
                except ValueError as e:
                    print(f"Error, {e}")
                    category = "Unknown"
                finally:
                    rowdict['Category'] = category
                    writer.writerow(rowdict)

        print(f"--- Finished to processing {input_filename} and {output_filename} ---")
    except FileNotFoundError:
        print(f"Error, file {input_filename} not found")

def main() -> None:
    """main function"""
    input_filename = "items.csv"
    output_filename = "items_output.csv"

    add_price_category(input_filename,output_filename)

if __name__ == "__main__":
    main()