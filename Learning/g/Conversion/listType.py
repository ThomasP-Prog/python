def convert_int(n :int|float|str) -> int|None:
    """Convert input to float if possible, otherwise return None."""
    try:
        return int(n) if isinstance(n,(int,float)) or (isinstance(n,str) and n.isdigit()) else None
    except (ValueError,TypeError):
        return None

def convert_float(n :float|str) -> float|None:
    """return input to float or None"""
    try:
        return float(n) if isinstance(n,(str,float)) else None
    except (ValueError,TypeError):
        return None

def convert_type(l :list) -> list:
    """return converted list changin type """
    new_list = []
    for i in l:
        if isinstance(i,str):
            converted_int = convert_int(i)
            if converted_int is not None:
                new_list.append(converted_int)
            else:
                converted_float = convert_float(i)
                if converted_float is not None:
                    new_list.append(converted_float)
                else:
                    new_list.append(i)
        else:
            new_list.append(i)
    return new_list

def main() -> None:
    """main function convert list and print result"""
    my_list = [1, "2", 3.5, "4.2", "five", 6]  
    converted_list = convert_type(my_list)  # Modify in place
    print(converted_list)  # ✅ Expected: [1, 2, 3.5, 4.2, "five", 6]
    for i in converted_list:
        print(type(i))  # ✅ Should print correct types
if __name__ == "__main__":
    main()