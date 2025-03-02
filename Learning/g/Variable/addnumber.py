def get_number() -> float | int:
    """ask input for new number"""
    while True:
        try:
            number = float(input("input a number : "))
            return int(number) if number == int(number) else number
        except ValueError:
            print("Number not valid")
        
def add_numbers(a :float|int,b :float|int) -> float|int: 
    """add numbers"""
    c = a+b
    return c

def main():
    print("main?")
    a = get_number()
    b = get_number()
    c = add_numbers(a,b)
    print(f"Types - a: {type(a)}, b: {type(b)}, c: {type(c)}")
    print(f"{a} + {b} = {c}")

if __name__ == "__main__":
    main()