import re

def get_name(prompt : str) -> str:
    """prompt user to enter contact name"""
    while True:
        try:
            new_input = input(prompt).strip()
            if new_input.replace("-","",1).replace("'","",1).isalpha():
                return new_input
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter name")

def get_email(prompt : str) -> str:
    """prompt user to enter contact email"""
    while True:
        try:
            new_input = input(prompt).strip()
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(pattern, new_input):
                return new_input
            elif not ".com" in new_input or not "@" in new_input:
                    print("Error. email need to enter a valid email adress")
        except ValueError:
            print("Error. Enter email")
               
                


def add_contact(contacts : dict) -> dict:
    """add a new contact"""
    contact_name = get_name("Enter new contact name : ")
    if contact_name not in contacts:
        contact_email = get_email("Enter new contact email : ")
        contacts[contact_name] = {'email' : {contact_email}}
        print("Contact added")
    else:
        print(f"{contact_name} already in the list")
    return contacts

def update_email(contacts : dict) -> dict:
    """update contact email"""
    contact_name = get_name("Enter name of contact to update : ")
    
    if contact_name in contacts:
        contact_email = get_email("Enter new email : ")
        contacts[contact_name]['email'] = contact_email
        print("Contact updated")
    else:
        print(f"{contact_name} not in the list")
    return contacts

def delete_contact(contacts : dict) -> dict:
    """delete a contact"""
    contact_name = get_name("Enter name of contact to delete : ")
    if contact_name in contacts:
        contacts.pop(contact_name)
        print(f"{contact_name} removed")
    else:
        print(f"No contact named {contact_name}")
    return contacts

def search_contact(contacts : dict) -> None:
    contact_name = get_name("Enter name of searched contact : ")
    if contact_name in contacts:
        info = contacts[contact_name]
        print(f"Name: {contact_name} | Email: {info.get('email', 'No email')}")
    else:
        print(f"No contact named {contact_name}")


def main() -> None:
    """main function"""
    contacts = {}
    contacts = add_contact(contacts)
    contacts = add_contact(contacts)
    contacts = update_email(contacts)
    contacts = delete_contact(contacts)
    search_contact(contacts)
    
if __name__ == "__main__":
    main()