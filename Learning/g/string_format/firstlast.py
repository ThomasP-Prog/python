def get_name(prompt :str) -> str:
    """prompt user name and validate"""
    while True:
        try:
            user_input = input(prompt).strip().capitalize()
            if not user_input:
                print("Name cannot be empty")
                continue
            if not user_input.replace(" ","").replace("-","").isalpha():
                print("Names cannot contain numbers or special characters (except spaces and hyphens).")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting.")
            exit(0)

def main() -> None:
    """main function"""
    first_name = get_name("Enter your first name : ")
    last_name = get_name("Enter your last name : ")
    print(f"Hello {first_name} {last_name}")

if __name__ == "__main__":
    main()