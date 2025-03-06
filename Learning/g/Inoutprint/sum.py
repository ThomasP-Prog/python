def get_number() -> list:
    """prompt user to enter numbers exit when prompted"""
    l = []
    while True:
        num = input("Enter a number or exit to get number sum :")
        if num.lower() == "exit":
            return l
        try:
            float_num = float(num)
            if float_num.is_integer():
                l.append(int(float_num))
            else:
                l.append(float_num)
        except ValueError:
            print("Invalid input. Please enter a number or type 'exit' to finish.")

def main() -> None:
    """main function"""
    my_list = get_number()
    print(f"{my_list} sum : {sum(my_list)}")

if __name__ == "__main__":
    main()


