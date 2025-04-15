"""Write a function deep_freeze(data) that takes an arbitrarily nested data structure containing
   lists, dictionaries, sets, tuples, strings, and numbers. The function should return a new, 
   deeply immutable version of the structure where all lists are converted to tuples, 
   all sets to frozensets, and all dictionary keys and values are recursively "frozen" in the same manner.
   Ensure dictionary keys remain hashable (e.g., don't try to freeze a dictionary key that was originally a list)."""

from typing import Any

def deep_freeze(data : Any) -> Any:
    """takes an arbitrarily nested data structure and return immutable version"""
    if isinstance(data,list):
        # Transform list in tuple
        return tuple(deep_freeze(item) for item in data)
    elif isinstance(data,set):
        # Transform set in frozenset
        return frozenset(deep_freeze(item) for item in data)
    elif isinstance(data, dict):
    # Return a tuple of (frozen_key, frozen_value) pairs
    # Keys are assumed hashable/immutable already, just freeze values
        return tuple((key, deep_freeze(value)) for key, value in data.items())
    elif isinstance(data,tuple):
        # Transform items in tuples as tuple
        return tuple(deep_freeze(item) for item in data)
    elif isinstance(data, (int, float, str, bool, type(None), frozenset)):
        # Types that are immutable
        return data
    else:
        # Optional: Handle other types or raise an error for unsupported types
        raise TypeError(f"Unsupported type for deep_freeze: {type(data)}")

def print_data(data : dict) -> None:
    """print data"""
    print(data)


def main() -> None:
    """main function"""
    # Sample Input Data for deep_freeze:
    data_to_freeze = {
        "user_id": 123,
        "username": "coder1",
        "roles": ["admin", "editor"], # Mutable list
        "preferences": {
            "theme": "dark",
            "notifications": {"email", "push"}, # Mutable set
            "layout": ["sidebar", "header"]     # Mutable list inside dict
        },
        "login_history": [ # Mutable list of tuples (tuples are immutable)
            ("2025-04-10 10:00:00", "192.168.1.5"),
            ("2025-04-12 15:30:00", "10.0.0.3")
        ],
        "active_sessions": { # Mutable dict
            "session1": {"device": "laptop", "ip": "192.168.1.5"},
            "session2": {"device": "mobile", "ip": "10.0.0.3"}
        }
    }
    frozen_data = deep_freeze(data_to_freeze.copy())

    print_data(frozen_data)

if __name__ == "__main__":
    main()