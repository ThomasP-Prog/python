"""Create a function build_config(**settings) that accepts any keyword arguments representing configuration settings. 
   It should return a dictionary containing these settings, but it should only include settings where the value is not None"""

from typing import Dict,Any

def build_config(**settings : Any) -> Dict[str,Any]:
    """
    Builds a configuration dictionary from keyword arguments,
    excluding any items where the value is None

    Args:
        settings : arbitrary keyword arguments representing config

    Returns:
        A dictionnary containing only the settings that were not None
    """
    config = {key : value for key,value in settings.items() if value is not None}
    return config

def main() -> None:
    """main function"""
    config1 = build_config(host="localhost", port=8080, debug_mode=None, username="guest")
    print(config1)
    # Expected: {'host': 'localhost', 'port': 8080, 'username': 'guest'}

    config2 = build_config(timeout=30, max_retries=5, api_key=None)
    print(config2)
    # Expected: {'timeout': 30, 'max_retries': 5}

    config3 = build_config(color=None, size=None)
    print(config3)
    # Expected: {}

if __name__ == "__main__":
    main()