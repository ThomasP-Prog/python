"""Implement a simple caching system using dictionaries.
   Create a function decorator that memorizes the results of expensive function calls,
   storing results in a dictionary where the keys are the function arguments
   and the values are the function results. Make sure it works for functions with multiple arguments."""

def memoize(func):
    """
    A decorator that caches the results of function calls.
    """
    # Create a cache dictionary to store results
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create a hashable key from the arguments
        # For kwargs, we need to sort to ensure consistent ordering
        key = (args, tuple(sorted(kwargs.items())))
        
        # Check if result is already in cache
        if key not in cache:
            print(f"Cache miss for {func.__name__}{args}. Computing...")
            # Compute and store result
            cache[key] = func(*args, **kwargs)
        else:
            print(f"Cache hit for {func.__name__}{args}. Using stored value.")
        
        return cache[key]
    
    return wrapper

# Example usage
@memoize
def fibonacci_recursive(n):
    """Compute fibonacci number recursively (expensive)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test with multiple calls
def main():
    # First call - should compute
    print(f"Result: {fibonacci_recursive(10)}")
    # Second call with same args - should use cache
    print(f"Result: {fibonacci_recursive(10)}")
    # Different args - should compute
    print(f"Result: {fibonacci_recursive(11)}")
    
    # Test with a function that takes multiple arguments
    @memoize
    def multiply_add(a, b, c):
        print("Executing expensive calculation...")
        return a * b + c
    
    print(multiply_add(3, 4, 5))  # Should compute
    print(multiply_add(3, 4, 5))  # Should use cache
    print(multiply_add(5, 4, 3))  # Should compute (different args)

if __name__ == "__main__":
    main()


    