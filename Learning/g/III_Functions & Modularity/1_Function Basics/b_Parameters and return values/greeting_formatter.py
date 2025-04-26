"""Define a function format_greeting that takes one parameter, name (a string). 
   Inside the function, create a greeting string like "Hello, [name]! Welcome aboard.". 
   Return this formatted string. Call the function with a sample name and print the returned greeting.

   Concepts Reinforced: Function definition, single parameter, string formatting within function, 
   return string value, calling with argument, printing returned value."""

def format_greeting(name : str) -> str:
    """format and return greeting"""
    return f"Hello, {name}! Welcome aboard."

def main() -> None:
    """main function"""
    greeting = format_greeting("Captain Eva")
    print(greeting)

if __name__ == "__main__":
    main()