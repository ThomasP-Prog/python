"""Define a function named check_key_value that takes three arguments: data_dict (a dictionary), 
   key_to_check (a string), and value_to_check. The function should check if the key_to_check exists 
   in the data_dict AND if its corresponding value is equal to value_to_check. 
   The function should return True if both conditions are met, and False otherwise. 
   Call the function with a sample dictionary and various keys/values to test different scenarios 
   (key exists/value matches, key exists/value differs, key doesn't exist) and print the boolean results.

   Concepts Reinforced: Function definition, dictionary parameter, string/other parameter types, 
   dictionary access (.get() or in check + direct access), conditional logic (if/else, and), return boolean."""

from typing import Dict, Any
_sentinel = object()

def check_key_value(data_dict : Dict[str,Any],key_to_check : str, value_to_check : str|int) -> bool:
    """check if key is in dict and if the value is correct"""
    
    if key_to_check in data_dict:
        if data_dict[key_to_check] == value_to_check:
            return True
    return False

def main() -> None:
    """main function"""
    user_data = {"name": "Alice", "status": "active", "level": 5}
    check = check_key_value(user_data, "status", "active") #-> Expected: True
    print(check)
    check = check_key_value(user_data, "level", 3) #-> Expected: False
    print(check)
    check = check_key_value(user_data, "email", "a@b.com") #-> Expected: False
    print(check)

if __name__ == "__main__":
    main()