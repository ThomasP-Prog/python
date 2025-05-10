"""
Write a function get_path_components(full_path_str: str) -> dict. This function takes a string representing 
an absolute or relative file path. Using pathlib (preferred) or os.path, extract the following components and return them in a dictionary:
    - 'directory': The path to the parent directory.
    - 'filename': The name of the file including the extension.
    - 'extension': The file extension (including the leading dot, or empty string if no extension).
"""
from pathlib import Path

def get_path_components(full_path_str: str) -> dict:
    """
    Returns a dict with the directory, filename and extension

    Args:
        full_path_str: str

    Returns:
        dict
    """
    path_obj = Path(full_path_str)

    return {
        'directory' : path_obj.parent,
        'filename' : path_obj.name,
        'extension' : path_obj.suffix 
    }

def main() -> None:
    """main function"""

path1 = "/usr/local/bin/my_script.py"
print(get_path_components(path1))
# Expected: {'directory': '/usr/local/bin', 'filename': 'my_script.py', 'extension': '.py'}

path2 = "data/report.txt" 
print(get_path_components(path2))
# Expected: {'directory': 'data', 'filename': 'report.txt', 'extension': '.txt'}

path3 = "archive.tar.gz"
print(get_path_components(path3))
# Expected: {'directory': '', 'filename': 'archive.tar.gz', 'extension': '.gz'} 
# (Note: pathlib/os.path treat '.tar.gz' differently - pathlib's .suffix is '.gz', os.path.splitext gives '.gz')

if __name__ == "__main__":
    main()