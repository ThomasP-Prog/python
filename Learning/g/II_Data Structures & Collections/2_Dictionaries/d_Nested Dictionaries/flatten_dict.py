'''Implement a function that can "flatten" a nested dictionary into a single-level dictionary
   where the keys are dot-separated paths (e.g., "Class A.John.grade"). Then implement a function
   that can reconstruct the original nested dictionary from the flattened one.'''


def flatten(students: dict, parent_key: str = '', sep: str = '.') -> dict:
    """flatten a dictionary"""
    if not students:
        return {}
    flat_dict = {}
    for key, val in students.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key # if parent key not empty = parent_key.key else key
        
        if isinstance(val, dict): # if val is a dict
            flat_dict.update(flatten(val, new_key, sep=sep))
        else:
            flat_dict[new_key] = val
    return flat_dict

def original(flat_dict: dict, sep: str = '.') -> dict:
    """Reconstruct a nested dictionary from a flattened one."""
    nested_dict = {}
    for key, value in flat_dict.items():
        key_parts = key.split(sep)
        current_level = nested_dict
        for part in key_parts[:-1]:
            current_level = current_level.setdefault(part, {})
        current_level[key_parts[-1]] = value
    return nested_dict

def main() -> None:
    """main function"""
    flat = {}
    students = {
    "Alice": {
        "age": 20,
        "major": "Computer Science",
        "grades": {
            "Math": 90,
            "Python": 95,
            "English": 88
        }
    },
    "Bob": {
        "age": 22,
        "major": "Mechanical Engineering",
        "grades": {
            "Math": 85,
            "Physics": 92,
            "English": 79
        }
    },
    "Charlie": {
        "age": 21,
        "major": "Business",
        "grades": {
            "Economics": 87,
            "Accounting": 91,
            "English": 84
        }
    }
}
    flat = flatten(students)
    print(flat)
    flat = original(flat)
    print(flat)
    
if __name__ == "__main__":
    main()