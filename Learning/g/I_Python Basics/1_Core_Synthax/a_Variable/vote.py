def eligible() -> None:
    while True:
        try:
            age = int(input("Enter your age : "))
            print("True") if age>=18 else print("False")
            return None
        except ValueError:
            print("Enter a valid number :")

def main():
    eligible()

if __name__ == "__main__":
    main()