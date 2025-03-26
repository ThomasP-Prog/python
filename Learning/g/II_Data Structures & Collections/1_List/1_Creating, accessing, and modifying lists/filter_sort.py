def create_list() -> list:
    number_list = []
    while True:
        try:
            number = input("add a number to the list and type 'end' when finished : ")
            if number != "end" and number.replace(".","").replace("-","").isdigit() == False:
                raise ValueError
            if number == "end":
                return number_list
            if number.replace(".","").replace("-","").isdigit():
                if number.replace("-","").isdigit():
                    number_list.append(int(number))
                else:
                    number_list.append(float(number))

        except ValueError:
            if not number =="end":
                print("Error. Add a number to the list and type 'end' when finished")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye.")
            exit()

def remove_duplicate(numbers : list) -> None:
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    numbers[:] = unique_numbers

def remove_below_ten(numbers : list) -> None:
    numbers_supp_ten = []
    for number in numbers:
        if number >= 10:
            numbers_supp_ten.append(number)
    numbers[:] = numbers_supp_ten

def main() -> None:
    numbers = create_list()
    if numbers:
        print(numbers)
        remove_duplicate(numbers)
        print(numbers)
        numbers.sort()
        print(numbers)
        remove_below_ten(numbers)
        print(numbers)

if __name__ == "__main__":
    main()