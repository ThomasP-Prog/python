def get_valid_input(prompt: str, valid_range: tuple[int, int] = None, valid_values: tuple[str, str] = None) -> int | str:
    while True:
        try:
            value = input(prompt).strip().lower()
            if valid_values:
                if value in valid_values:
                    return value
                else:
                    raise ValueError
            num = float(value)
            if not num.is_integer():
                raise ValueError
            num = int(num)
            if valid_range and not (valid_range[0] <= num <= valid_range[1]):
                raise ValueError
            return num
        except ValueError:
            print(f"Invalid input. Please enter a valid {'option' if valid_values else 'integer'}.")
        except KeyboardInterrupt:
            print("You have exited the program, goodbye")
            exit()
        
def apply_discount(price: float, is_student: bool, is_senior: bool, is_matinee: bool) -> float:
    discount = 0
    if is_student and is_matinee:
        discount = 0.20
    elif is_student or is_senior:
        discount = 0.10
    elif is_matinee:
        discount = 0.10

    final_price = price * (1 - discount)
    print(f"Final price: {final_price:.2f}€")
    return final_price

def main() -> None:
    price = 10
    age = get_valid_input("Enter your age : ",(1,120))
    student = get_valid_input("Are you a student ? ",valid_values=("yes", "no")) == "yes"
    time = get_valid_input("Enter time (0:24) : ",(0,24))
    
    is_student = age < 18 and student
    is_senior = age >= 65
    is_matinee = 8 <= time < 17

    price = 10
    price = apply_discount(price, is_student, is_senior, is_matinee)

if __name__ == "__main__":
    main()