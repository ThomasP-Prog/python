"""
Assume a CSV file employee_data.csv with columns EmployeeID, FirstName, LastName, StartDate (string in "YYYY-MM-DD" format). 
Write a function add_years_of_service(input_filename: str, output_filename: str). 
This function should read the input CSV, calculate "YearsOfService" based on StartDate relative to a fixed "current date" 
(e.g., assume today is "2025-05-10" for consistency in calculation), and write a new CSV to output_filename that includes 
all original columns plus the new YearsOfService (integer, rounded down) column. Use datetime for date parsing and calculations. 
Handle ValueError for invalid date strings (write "N/A" for YearsOfService for that row). Handle FileNotFoundError.
"""

import csv
from pathlib import Path
from datetime import datetime

def add_years_of_service(input_filename: str, output_filename: str) -> None:
    """
    Make a new file adding the row 'YearsOfService' to 'emplyee_data.csv'

    Args:
        input_filename: str
        output_filename: str

    Returns:
        None
    """
    file_directory = Path(__file__).parent
    input_path = file_directory / input_filename
    output_path = file_directory / output_filename

    current_date = datetime.today()

    try:
        with open(input_path,mode='r', encoding='utf-8', newline='') as infile ,\
             open(output_path,mode='w', encoding='utf-8', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['EmployeeID','FirstName','LastName','StartDate','YearsOfService']
            writer = csv.DictWriter(outfile,fieldnames=fieldnames)
            writer.writeheader()

            for row_dict in reader:
                try:
                    employee_id = row_dict.get('EmployeeID','None')
                    first_name = row_dict.get('FirstName','None')
                    last_name = row_dict.get('LastName','None')
                    start_date = row_dict.get('StartDate','None')
                    start_date_obj = datetime.fromisoformat(start_date)
                    year = current_date.year - start_date_obj.year
                    month = current_date.month - start_date_obj.month
                    day = current_date.day - start_date_obj.day

                    if month < 0:
                        year -= 1
                    elif month == 0 and day < 0:
                        year -= 1

                except ValueError:
                    print(f"Warning, {employee_id} '{first_name}' '{last_name}' as an invalid date : '{start_date}'")
                    year = 'N/A'
                finally:
                    row_dict['YearsOfService'] = year
                    writer.writerow(row_dict)

    except FileNotFoundError as e:
        print(f"Error, {e}")
        
def main() -> None:
    """main function"""
    input_filename = "employee_data.csv"
    output_filename = "employee_data_output.csv"
    add_years_of_service(input_filename,output_filename)

if __name__ == "__main__":
    main()
