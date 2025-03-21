def get_input(prompt :str, data_type :type = str) -> str|int|float:
    """Prompt user to enter a value and validater with accepted type"""
    while True:
        try:
            user_input = input(prompt).strip()

            if data_type in [int,float] and float(user_input) > 0:
                if user_input.isdigit():
                    return int(user_input)
                else:
                    return float(user_input)
            else:
                if not user_input.replace("'","").replace("-","").isalpha():
                    raise ValueError
                return user_input
        except ValueError:
            if data_type in [int,float]:
                print("Error. Enter a number.")
            else:
                print("Error. Enter your name.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def add_user(users :dict) -> dict:
    """Fills dict with user input"""
    name = get_input("Enter your name : ")
    age = get_input("Enter your age : ",int)
    height = get_input("Enter your height in meters : ",float)

    users[name] = {'age' : age,
                   'height' : height}
    return users

def next_user() -> bool:
    """Check if user want to make another entry"""
    while True:
        try:
            choice = get_input("do you want to enter another entry ? (yes/no) ").strip()
            if choice == 'y' or choice == 'yes':
                return True
            elif choice == 'n' or choice == 'no':
                return False
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter yes or no.")
        except KeyboardInterrupt:
            print("\nYou exited the program. Goodbye.")
            exit()

def print_users(users :dict) -> None:
    """Print dict"""
    print(f"{'Name':<20} {'Age':<5} {'Height':>5} ")
    print("-"*33)
    for name,details in users.items():
        age = details.get("age","N/A")
        height = details.get("height","N/A")
        print(f"{name:<20} {age:<5} {height:>5}")

def main() -> None:
    """main function"""
    users = dict()
    new_user = True
    while new_user:
        users = add_user(users)
        new_user = next_user()
        print_users(users)

if __name__ == "__main__":
    main()
