"""
Define a class Counter.

    In its __init__, initialize an instance attribute count to 0.
    Add a method increment() that increases count by 1.
    Add a method get_value() that returns the current count.

Sample Usage: Create an instance, increment it a few times, and print its value.
"""

class Counter:
    def __init__(self):
        """Initialize the counter"""
        self.count = 0

    def increment(self):
        """increment the counter"""
        self.count += 1

    def get_value(self) -> int:
        """
        Returns the value of the counter
        
        Returns
            int
        """
        return self.count

def main() -> None:
    """main function"""
    new_counter = Counter()
    for _ in range(5):
        new_counter.increment()
    counter_value = new_counter.get_value()
    print(f"Counter value : {counter_value}")

if __name__ == "__main__":
    main()