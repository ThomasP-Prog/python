"""
Write a function categorize_paths(path_strings: list[str]) -> dict. The input is a list of path strings. 
Iterate through the list. For each path string, use pathlib (preferred) or os.path methods to determine 
if the path represents: a) An existing file. b) An existing directory. c) A path that does not exist. 
Return a dictionary summarizing the results, like: 
{'files': [list_of_file_paths], 'directories': [list_of_dir_paths], 'non_existent': [list_of_non_existent_paths]}.

Important Note: Since we can't interact with a real file system here, you will need to simulate the existence checks. 
For the purpose of the exercise, assume any path ending in .txt or .csv "exists as a file", any path not containing 
a . "exists as a directory", and anything else "does not exist". Implement the logic based on these simulation rules, 
but use the actual pathlib/os.path functions conceptually in your explanation if needed.
"""

from pathlib import Path

def categorize_paths(path_strings: list[str]) -> dict:
    """
    
    """
    list_of_file_paths = []
    list_of_dir_paths = []
    list_of_non_existent_paths = []

    """for new_path in path_strings:
        current_path = Path(new_path)
        if current_path.is_file():
            list_of_file_paths.append(new_path)
        elif current_path.is_dir():
            list_of_dir_paths.append(new_path)
        else:
            list_of_non_existent_paths.append(new_path)"""
    
    for new_path in path_strings:
        current_path = Path(new_path)
        if new_path.endswith('.txt') or new_path.endswith('.csv'):
            list_of_file_paths.append(new_path)
        elif "." not in current_path.name:
            list_of_dir_paths.append(new_path)
        else:
            list_of_non_existent_paths.append(new_path)

    return {'files' : list_of_file_paths,
            'directories' : list_of_dir_paths,
            'non_existent': list_of_non_existent_paths
            }

def main() -> None:
    """main function"""

    path_list = [
        "/home/user/docs/",    # Assume exists (dir)
        "data/input.csv",      # Assume exists (file)
        "/temp/my_app",        # Assume exists (dir)
        "output.log",          # Assume does not exist
        "../backup/archive.zip", # Assume does not exist
        "results.txt"          # Assume exists (file)
    ]
    print(categorize_paths(path_list))

if __name__ == "__main__":
    main()

# Expected Output (based on simulation rules):
# {
#  'files': ['data/input.csv', 'results.txt'], 
#  'directories': ['/home/user/docs/', '/temp/my_app'], 
#  'non_existent': ['output.log', '../backup/archive.zip']
# }