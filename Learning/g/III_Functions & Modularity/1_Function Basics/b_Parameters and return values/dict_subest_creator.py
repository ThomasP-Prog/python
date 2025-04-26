"""Define a function create_subset_dict that takes two parameters: original_dict (a dictionary) 
   and keys_to_include (a list of strings). The function should create and return a new dictionary 
   containing only the key-value pairs from original_dict where the key is present in the keys_to_include list. 
   If a key from keys_to_include is not found in original_dict, it should simply be ignored.

   Concepts Reinforced: Function definition, parameters (dictionary, list), creating a new dictionary, 
   iterating through a list (keys_to_include), checking key existence in a dictionary (in), 
   accessing dictionary values, adding to a new dictionary, return dictionary value."""

from typing import Dict,Any

def create_subset_dict(original_dict : Dict[str,Any], keys_to_include : list[str]) -> Dict[str,Any]:
    """
    create and return new dict of key-value pair from keys_to_include matching with the dict

    Args:
    original_dict : existing dict
    keys_to_include : keys that need to be checked

    Returns:
    dict of key-value pairs
    
    """
    if not original_dict:
        return dict()
    subset_dict = {key : original_dict[key] for key in keys_to_include if key in original_dict}
    #for key in keys_to_include:
    #    if key in original_dict:
    #        subset_dict[key] = original_dict[key]
    return subset_dict

def main() -> None:
    """main function"""

    full_data = {"name": "Alice", "age": 30, "city": "New York", "email": "alice@example.com"}
    desired_keys = ["name", "email", "country"] # Note: 'country' is not in full_data
    subset = create_subset_dict(full_data, desired_keys)
    print(subset)
    # Expected Output: When printing subset, it should display {'name': 'Alice', 'email': 'alice@example.com'}

if __name__ == "__main__":
    main()