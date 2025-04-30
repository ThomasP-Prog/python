"""
Describe calculator.py: This file should import the basic_math module. 
It should then call the add function with two numbers and print the result, 
and call the multiply function with two different numbers and print the result
"""

import basic_math as bm

def main() -> None:
    """main function"""
    a = 5
    b = 3
    print(f"{a} + {b} : {bm.add(a,b)}")
    print(f"{a} * {b} : {bm.multiply(a,b)}")

if __name__ == "__main__":
    main()