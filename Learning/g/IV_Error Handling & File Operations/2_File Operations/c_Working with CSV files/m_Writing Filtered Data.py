"""
Write a function write_active_users(input_filename: str, output_filename: str). 
Assume input_filename points to a CSV with columns UserID, Name, Status. 
Read the input file using csv.reader (or DictReader). 
Write a new CSV file to output_filename using csv.writer that includes only the rows where the Status column is equal to "active". 
Make sure to include the header row in the output file. Handle potential FileNotFoundError.
"""

import csv
from pathlib import Path

def write_active_users(input_filename: str, output_filename: str) -> None:
    """
    
    """
    file_directory = Path(__file__).parent
    read_path = file_directory / input_filename
    write_path = file_directory / output_filename

    try:
        print(f"--- Attempting to process {input_filename} and {output_filename} ---")
        with open(read_path, mode='r',encoding='utf-8',newline='') as infile, \
            open(write_path,mode='w',encoding='utf-8',newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            header = ['UserID', 'Name', 'Status']
            writer.writerow(header)

            for row_dict in reader:
                is_active = row_dict.get('Status','None')
                if is_active == 'active':
                    output_values = [row_dict.get(header[0],''),
                                     row_dict.get(header[1],''),
                                     row_dict.get(header[2],'')]
                    writer.writerow(output_values)
        print(f"--- Finished to process {input_filename} and {output_filename} ---")
    except FileNotFoundError:
        print(f"Error, {input_filename} does't exist")

def main() -> None:
    """main function"""
    input_filename = "users.csv"
    output_filename = "users_output.csv"
    write_active_users(input_filename,output_filename)
        
if __name__ == "__main__":
    main()
