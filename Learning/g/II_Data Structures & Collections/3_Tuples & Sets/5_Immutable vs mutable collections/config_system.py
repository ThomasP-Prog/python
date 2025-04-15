"""You are designing a configuration system where default configurations are stored (and should never change), 
   but users can provide overrides that can change. Implement a function get_effective_config(defaults, overrides) 
   where defaults is a potentially nested structure (using immutable types like tuples where possible) and overrides 
   is a dictionary (mutable) providing user changes. The function should return the final configuration, 
   prioritizing overrides but falling back to defaults. The challenge is to ensure that the returned configuration 
   reflects the overrides correctly but without modifying the original defaults structure, 
   even if overrides target nested mutable parts that might conceptually exist within the defaults (if they were mutable). 
   Consider how to safely merge these structures respecting mutability."""

import copy

def get_effective_config(defaults : dict, overrides : dict) -> dict:
    """Overrides default configuration"""

    if not overrides:
        return copy.deepcopy(defaults)

    config = copy.deepcopy(defaults)
    for key,value in overrides.items():
        if key in defaults and isinstance(defaults[key],dict) and isinstance(value,dict): # Use recursion if nested dict
            config[key] = get_effective_config(config[key],value)
        else:
            config[key] = copy.deepcopy(value)
    return config

def print_config(config_dict, indent=0):
    """Recursively prints a nested dictionary with indentation."""
    indent_space = "  " * indent
    for key, value in config_dict.items():
        if isinstance(value, dict):
            print(f"{indent_space}{key}:")
            print_config(value, indent + 1)
        elif isinstance(value, (tuple, set, frozenset)):
            print(f"{indent_space}{key}: {sorted(list(value))}") # Example
        else:
            print(f"{indent_space}{key}: {value}")

def main() -> None:
    """main function"""

    default_config = {
        'api_version': 1,
        'timeout_seconds': 30,
        'enabled_features': frozenset(['feature_A', 'feature_B']), # Immutable set
        'server_settings': { # Nested dictionary
            'host': 'api.example.com',
            'port': 443,
            'allowed_methods': ('GET', 'POST') # Immutable tuple
        },
        'user_roles': ('guest',) # Immutable tuple
    }

    # User overrides (mutable dictionary, potentially incomplete)
    user_overrides = {
        'timeout_seconds': 60, # Override a top-level value
        'enabled_features': {'feature_A', 'feature_C'}, # Override with a mutable set
        'server_settings': { # Override a nested dictionary (partially)
            'port': 8443 
        }
        # 'user_roles' and 'api_version' are not overridden
    }
    config = (get_effective_config(default_config,user_overrides))
    print_config(config)

if __name__ == "__main__":
    main()