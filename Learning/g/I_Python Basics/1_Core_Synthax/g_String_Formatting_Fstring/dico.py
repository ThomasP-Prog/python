def print_dic(user_details :list[tuple]) -> None:
    """print dictionnary"""
    if not user_details:
        print("list empty")
        return
    
    #Header
    print(f"{'Name':<20} {'Age':<5} {'Email':<30}")
    print("-" * 50)

    for name, details in user_details.items():
        age = details.get("age","N/A")
        email = details.get("email","N/A")
        print(f"{name:<20} {age:<5} {email:<30}")

def main():
    """main function"""
    users = {
        "Thomas": {"age":19,"email":"thomas@adress.com"},
        "Bob": {"age": 10,"email":"bob@adress.com"}
    }
    print_dic(users)

if __name__ == "__main__":
    main()