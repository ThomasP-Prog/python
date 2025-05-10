"""
Assume a CSV file sensor_readings.csv with columns SensorID (string) and Value (string, expected to be a number). 
Write a function get_high_readings(filename: str, value_threshold: float) -> list[tuple[str, float]]. 
The function should read the file, and for each row, attempt to convert Value to a float. 
If successful and the float value is greater than value_threshold, add a tuple (SensorID, ValueAsFloat) to a result list. 
Skip rows where Value cannot be converted to a float (print a warning). Handle FileNotFoundError.
"""

import csv
from pathlib import Path
from typing import List,Tuple

def get_high_readings(filename: str, value_threshold: float) -> List[Tuple[str, float]]:
    """
    Returns a list of tuple SensorID,Value of Value is greater then threshold

    Args:
        filename: str, value_threshold: float

    Returns
        List[Tuple[str, float]]
    """
    file_directory = Path(__file__).parent
    full_path = file_directory / filename
    sensor_list = []

    try:
        print(f"--- Attempting to process {filename} ---")
        with open(full_path, mode="r", encoding="utf-8", newline='') as infile:
            reader = csv.DictReader(infile)

            for row_dict in reader:
                try:
                    value = row_dict.get('Value','None')
                    sensor_id = row_dict.get('SensorID','None')
                    float_value = float(value)

                    if float_value > value_threshold:
                        sensor_list.append((sensor_id,float_value))
                except ValueError:
                    print(f"Warning, SensorID '{sensor_id}' has an invalid value: '{value}'")
        print(f"--- Finished processing {filename} ---")
    except FileNotFoundError as e:
        print(f"Error, {e}")
    return sensor_list

def main() -> None:
    """main function"""

    sensor_result = get_high_readings("sensor_readings.csv", 23.0)
    print(sensor_result)

if __name__ == "__main__":
    main()