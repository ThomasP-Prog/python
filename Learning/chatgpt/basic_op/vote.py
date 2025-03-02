def user_age() -> int:
    while True:
        try:
            return int(float(input("Entrer your age : ")))
        except ValueError:
            print("Wrong number")

def is_eligible(age : int) -> None:
    if age >= 18:
        print("You can vote.")
    else:
        print("You can't vote")

def main() -> None:
    age = user_age()
    is_eligible(age)

if __name__ == "__main__":
    main()