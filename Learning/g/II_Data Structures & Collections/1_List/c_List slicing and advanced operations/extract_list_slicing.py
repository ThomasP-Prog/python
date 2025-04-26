def extract_first_ten(elements : list) -> list:
    return elements[: min(10, len(elements))]

def extract_every_third(elements : list) -> list:
    return elements[::3]

def extract_reverse_last_five(elements :list) -> list:
    return elements[-1: -min(6, len(elements) + 1): -1]


def main() -> None:
    elements = list(range(1, 21))
    
    print(f"elements : {elements}")
    first_ten = extract_first_ten(elements)
    print(f"first ten elements : {', '.join(map(str, first_ten))}")
    every_third = extract_every_third(elements)
    print(f"every third elements: {', '.join(map(str, every_third))}")
    reverse_five = extract_reverse_last_five(elements)
    print(f"reverse five last elements : {', '.join(map(str, reverse_five))}")

if __name__ == "__main__":
    main()