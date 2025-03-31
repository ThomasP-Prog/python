"""Write a function that creates a "nested" phone book where each person
   can have multiple contact numbers (home, work, mobile).
   Include functionality to add contacts, update numbers,
   and search for people by partial name matches."""

import re

def get_name() -> str:
    while True:
        try:
            name = input("Enter name :").strip()
            if not name:
                raise ValueError
            else:
                if name.replace("'","",1).replace("-","",1).isalpha():
                    return name
                else:
                    raise KeyError
        except ValueError:
                print("Error. name can't be empty.")
        except KeyError:
            print("Error. name can only contain - or ' as special caracter.")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye")
            exit()

def as_phone(phone_type : str, is_new : str = "false") -> bool:
    while True:
        try:
            if is_new == "false":
                answer = input(f"Do you have a {phone_type} number ? yes/no : ").strip()
            elif is_new == "true":
                answer = input(f"Do you  want to enter new {phone_type} number ? yes/no : ").strip()
            else:
                answer = input(f"Do you  search for {phone_type} ? yes/no : ").strip()
            if not answer:
                raise ValueError
            else:
                if answer == "yes":
                    return True
                elif answer == "no":
                    return False
                else:
                    raise ValueError
        except ValueError:
                print("Error. Enter 'yes' or 'no'.")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye")
            exit()

def get_phone(prompt : str) -> int:
    while True:
        try:
            phone = input(f"Enter {prompt} phone number : ")
            if phone.isdigit():
                if len(phone) == 10:
                    return int(phone)
                else:
                    print("Phone number as to have 10 numbers")
            else:
                raise ValueError
        except ValueError:
            print("Error. Phone number as to only contain numbers.")
        except KeyboardInterrupt:
            print("You exited the program. Goodbye")
            exit()

def add_contact(phonebook : dict) -> dict:
    name = get_name()
    if name in phonebook:
        print(f"{name} is already in the phonebook.")
    else:
        as_home = as_phone("home")
        if as_home:
            home = get_phone("home")
        else:
            home = None
        as_work = as_phone("work")
        if as_work:
            work = get_phone("work")
        else:
            work = None
        as_mobile = as_phone("mobile")
        if as_mobile:
            mobile = get_phone("mobile") 
        else:
            mobile = None   
    
        phonebook[name] = {"home" : home,
                        "work" : work,
                        "mobile" : mobile}
        return phonebook

def update_phone(phonebook : dict) -> dict:
    name = get_name()
    if name not in phonebook:
        print(f"{name} isn't in the phonebook.")
        return phonebook
    else:
        as_home = as_phone("home",True)
        if as_home:
            phonebook[name]['home'] = get_phone("home")
        as_work = as_phone("work",True)
        if as_work:
            phonebook[name]['work'] = get_phone("work")
        as_mobile = as_phone("mobile",True)
        if as_mobile:
            phonebook[name]['mobile'] = get_phone("mobile")
    return phonebook
 
def search_name(phonebook : dict) -> str|None:
    searched_name = get_name()
    pattern = rf"\b\w*{searched_name}\w*\b"
    names = [name for name in phonebook]
    for _ in range(0,len(names)):
        found_name = re.findall(pattern,names[_])
        if found_name:
            print(f"Do you search for {found_name[0]} ?")
            found = as_phone(found_name[0],"other")
            if found:
                return found_name[0]
    print("User not found")

def main() -> None:
    phonebook = {}
    add_contact(phonebook)
    #print(phonebook)
    #update_phone(phonebook)
    print(phonebook)
    search_name(phonebook)

if __name__ == "__main__":
    main()