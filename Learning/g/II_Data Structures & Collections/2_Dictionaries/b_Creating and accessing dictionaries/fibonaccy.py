fib_cache = {}

def fib(n : int) -> int:
    if n in fib_cache:
        print("computed")
        print(fib_cache[n])
        print(f"cache : {fib_cache}")
        return fib_cache[n]
    if n <= 1:
        return n
    fib_cache[n] = fib(n-1) + fib(n-2)
    print("calculate")
    print(fib_cache[n])
    return fib_cache[n]

def main() -> None:
    print(fib(35))

if __name__ == "__main__":
    main()