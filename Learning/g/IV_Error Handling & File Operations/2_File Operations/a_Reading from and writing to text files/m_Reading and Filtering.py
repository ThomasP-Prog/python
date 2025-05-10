"""
Assume you have a text file named data.txt. Write a function find_lines_with_word(filename: str, word: str) -> list[str]. 
The function should open the file specified by filename in read mode ('r') using with open(). 
Iterate through the lines of the file. 
Return a list containing only those lines (including their original newline characters, if any) 
that contain the specified word (case-sensitive). Handle FileNotFoundError by printing an error message and returning an empty list.
"""

from pathlib import Path

def find_lines_with_word(filename: str, word: str) -> list[str]:
    """
    Returns a list of the lines with the keyword

    Args:
        filename: str
        word: str
    
    Returns:
        list[str]
    """
    script_directory = Path(__file__).parent
    full_path = script_directory / filename
    line_list = []
    try:
        print(f"--- Attempting to read to {filename} ---")
        with open(full_path,mode='r',encoding='utf-8') as infile:
            for line in infile:
                if word in line:
                    line_list.append(line)
        print(f"--- Reading Successful ---")
    except FileNotFoundError as e:
        print(f"Error, {e}")
    except Exception as e:
        print(f"Error, {e}")
    return line_list


def main() -> None:
    """main function"""
    python_lines = find_lines_with_word("data.txt", "Python")
    print(python_lines)
    # Expected output: ['Python is fun.\n'] 
    # (Assuming case-sensitive match, adjust if case-insensitivity desired)

    # Conceptual call:
    line_lines = find_lines_with_word("data.txt", "line")
    print(line_lines)
    # Expected output: ['This is the first line.\n', 'This line contains python too.\n', 'Another line here.\n']

    # Conceptual call:
    missing_lines = find_lines_with_word("nonexistent.txt", "word")
    print(missing_lines)
    # Expected: Prints error, returns []

if __name__ == "__main__":
    main()