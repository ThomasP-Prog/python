def even_reversed(numbers : list) -> list:
    """new_list = []
    for n in numbers:
        if n%2 == 0:
            new_list.append(n)
    return new_list[::-1]"""
    return [n for n in numbers if n % 2 == 0][::-1]

def main() -> None:
    numbers = list(range(0,20))
    print(f"numbers : {', '.join(map(str,numbers))}")
    new_list = even_reversed(numbers)
    print(f"new list of numbers : {', '.join(map(str,new_list))}")

if __name__ == "__main__":
    main()