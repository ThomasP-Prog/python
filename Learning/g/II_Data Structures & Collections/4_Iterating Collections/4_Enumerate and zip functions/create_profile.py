"""Write a function create_profiles(names, emails) that takes two lists: names (strings) and emails (strings), 
   assumed to be of the same length. Use zip to iterate through them simultaneously. 
   Create and return a list of dictionaries, where each dictionary represents a profile with "name" and "email" keys.

   Concepts Reinforced: zip, lists, dictionaries, loop, function definition, returning a list of dictionaries."""

def create_profiles(names : list[str], emails : list[str]) -> list[dict[str,str]]:
    """return a list of dict with name and email keys"""
    if not names or not emails:
        return []
    
    user_info = [{"name" : name,"email" : email} for name,email in zip(names,emails)]
    return user_info

def print_info(user_info : list[dict[str,str]]) -> None:
    """Format user info"""
    if not user_info:
        return
    
    print("Users informations")
    for user in user_info:
        print(f"Name : {user.get('name','')}")
        print(f"Email : {user.get('email','')}")

def main() -> None:
    """main function"""


    user_names = ["Claire", "Max", "Lena"]
    user_emails = ["claire@email.com", "max@mail.org", "lena@web.net"]
    # Expected Output:
    # [
    #   {'name': 'Claire', 'email': 'claire@email.com'},
    #   {'name': 'Max', 'email': 'max@mail.org'},
    #   {'name': 'Lena', 'email': 'lena@web.net'}
    # ]
    user_info = create_profiles(user_names,user_emails)
    print_info(user_info)

if __name__ == "__main__":
    main()