def replace_even(elements : list) -> list:
    """Replace even indices with 0"""
    elements[::2] = [0] * len(elements[::2])
    return elements

def remove_middle_third(elements : list) -> list:
    del elements[len(elements)//3 : 2*len(elements)//3]
    return elements

def main() -> None:
    elements = list(range(1, 21))
    print(f"elements : {', '.join(map(str,elements))}")
    elements = replace_even(elements)
    print(f"replaced elements : {', '.join(map(str,elements))}")
    elements = remove_middle_third(elements)
    print(f"removed middle third elements : {', '.join(map(str,elements))}")

if __name__ == "__main__":
    main()