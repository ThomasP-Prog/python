"""
Write a function get_user_info(user_database: dict, user_id: str) -> str. 
The user_database is a dictionary where keys are user IDs (strings) and values are dictionaries containing user details 
(e.g., {'name': 'Alice', 'age': 30}). The function should try to retrieve the user's details dictionary using the user_id. 
Then, it should try to get the 'name' from the details dictionary.
    - Use try...except KeyError to handle cases where the user_id is not in user_database OR where the user's details dictionary 
    doesn't contain a 'name' key. In these cases, return "User or name not found."
    - Use try...except TypeError to handle the case where the value associated with user_id might not be a dictionary 
    (e.g., it's None or a string), preventing access like details['name']. In this case, also return "Invalid data structure for user."
    - If successful, return the user's name
"""

def get_user_info(user_database: dict, user_id: str) -> str:
    """
    Return the name linked to user_id or return a string with the error

    Args:
        user_database: dict
        user_id: str)
        
    Returns:
        str
    """
    try:
        user_details =  user_database[user_id] # Raise KeyError if user_id not found

        if not isinstance(user_details,dict):
            raise TypeError
        
        user_name = user_details['name'] # Raise KeyError if 'name' key missing
        
        if not isinstance(user_name,str):
            raise TypeError
        
        return user_name
         
    except KeyError:
        return "User or name not found."
    except TypeError:
        return "Invalid data structure for user."

def main() -> None:
    """main function"""

    database = {
        "id001": {"name": "Alice", "age": 30},
        "id002": {"age": 25}, # Missing 'name' key
        "id003": None,        # Not a dictionary
        "id004": {"name": 123, "age": 40} # Name is not a string
    }
    print("--- Using Idiomatic Version ---")
    name1 = get_user_info(database, "id001") # Expected: "Alice"
    name2 = get_user_info(database, "id002") # Expected: "User or name not found." (KeyError on 'name')
    name3 = get_user_info(database, "id003") # Expected: "Invalid data structure for user." (TypeError)
    name4 = get_user_info(database, "id005") # Expected: "User or name not found." (KeyError on user_id)
    name5 = get_user_info(database, "id004") # Expected: "Invalid data structure for user." (TypeError - name not str)
    print(f"id001: {name1}")
    print(f"id002: {name2}")
    print(f"id003: {name3}")
    print(f"id005: {name4}")
    print(f"id004: {name5}")

if __name__ == "__main__":
    main()