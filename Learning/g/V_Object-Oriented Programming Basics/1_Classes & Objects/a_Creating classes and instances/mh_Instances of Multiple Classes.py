"""
Define three simple classes: CPU (with pass), RAM (with pass), and HardDrive (with pass). 
Now define a class Computer (with pass). 
Write a function build_computer_components() that creates one instance of CPU, two distinct instances of RAM, 
one instance of HardDrive, and one instance of Computer. 
The function should then return a dictionary where the keys are descriptive strings 
(e.g., "processor", "memory_stick_1", "memory_stick_2", "storage", "main_system") and the values are the corresponding created instances. 
In your main function, call build_computer_components() and print the type of each component retrieved from the returned dictionary.
"""
from typing import Dict,Any

class CPU:
    pass
class RAM:
    pass
class HardDrive:
    pass
class Computer:
    pass

def build_computer_components() -> Dict[str,Any]:
    """
    Build a computer with a CPU, two RAM, a storage and a main system

    Args:
        None

    Returns:
        Dict[str,Any]
    """
    return {
        'processor' : CPU(),
        'memory_stick_1' : RAM(),
        'memory_stick_2' : RAM(),
        'storage' : HardDrive(),
        'main_system' : Computer()
    }

def print_computer_dict(computer_dict : Dict[str,Any]) -> None:
    """
    Prints the computer dict

    Args:
        Dict[str,Any]

    Returns
        None
    """
    if computer_dict:
        for name,component in computer_dict.items():
            print(f"{name} : {type(component)}")

def main() -> None:
    """main function"""
    computer_dict = build_computer_components()
    print_computer_dict(computer_dict)

if __name__ == "__main__":
    main()
