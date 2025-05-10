"""
Write a function build_project_paths(project_name: str) -> dict. Imagine a standard project structure where you have a main project directory, 
and inside it, subdirectories named src, data, and docs. The function takes the project_name string. Using pathlib (preferred) or os.path, 
construct relative path strings for the following, assuming the current context is inside the main project directory:
    - The source directory (src).
    - A main script file inside src called main.py.
    - An input data file inside data called input.csv.
    - A documentation file inside docs called readme.md. Return these four path strings in a dictionary keyed by 'source_dir', 'main_script', 'data_file', 'docs_file'.
"""

from pathlib import Path

def build_project_paths(project_name: str) -> dict:
    """
    Returns a dict of the path from source_dir,main_script,data_file and docs_file

    Args:
        project_name : str

    Returns dict
    """
    project_root = Path('.')

    src_dir = project_root / 'src'
    main_script_path = src_dir / 'main.py'
    data_file_path = project_root / 'data' / 'input.csv'
    docs_file_path = project_root / 'docs' / 'readme.md'


    return {
        'source_dir' : str(src_dir),
        'main_script': str(main_script_path),
        'data_file': str(data_file_path),
        'docs_file': str(docs_file_path)
    }

def main() -> None:
    """main function"""

    project = "MyCoolProject"
    build = build_project_paths(project)
    print(build)

if __name__ == "__main__":
    main()

# Expected output (paths will use OS-specific separators):
# {
#  'source_dir': 'src', 
#  'main_script': 'src/main.py' OR 'src\\main.py',
#  'data_file': 'data/input.csv' OR 'data\\input.csv',
#  'docs_file': 'docs/readme.md' OR 'docs\\readme.md'
# }