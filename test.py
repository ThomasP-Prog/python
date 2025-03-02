# This is a simple Python script
# this is a comment
# and this is not 
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))


def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
 
    

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)