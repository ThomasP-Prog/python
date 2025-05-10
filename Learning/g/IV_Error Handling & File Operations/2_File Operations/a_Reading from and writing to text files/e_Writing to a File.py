"""
Write a function save_list_to_file(filename: str, data: list). The function should take a filename (string) 
and a list of items. Using with open() in write mode ('w'), write each item from the list to the file, 
with each item on a new line. Convert items to strings if necessary.
"""
from pathlib import Path # Import Path

def save_list_to_file(filename: str, data: list) -> None:
    """
    Save the list in the file

    Args:
        filename: str
        data: list

    Returns:
        None
    """
    script_directory = Path(__file__).parent # Get directory where the current file is
    full_path = script_directory / filename # Make the full path ( directory + filename)
    try:
        print(f"--- Attempting to write to {filename} ---")
        with open(full_path, mode='w',encoding='utf-8') as outfile:
            for line in data:
                new_line = str(line)+'\n'
                outfile.write(new_line)
        print(f"Successfully wrote {len(data)} lines.")
    except Exception as e:
        print(f"Error, {e}")

def main() -> None:
    """main function"""
    my_items = ["apple", 123, True, 3.14]
    save_list_to_file("output_easy.txt", my_items)
if __name__ == "__main__":
    main()

# Expected content of 'output_easy.txt':
# apple
# 123
# True
# 3.14

