"""
Write a function find_first_valid_email(emails: list[str | None]) -> str | None. The input is a list potentially containing strings or None. Iterate through the list. For each email:

    Use try...except...finally.
    try: Check if the email is a string AND contains "@". If both are true, print "Valid email found!" and immediately return the email string.
    except TypeError: (This might occur if email is not a string and you try string methods like in on it). Print a message like "Skipping non-string item: [item]". Use continue inside this except block to move to the next item.
    finally: Inside the loop, always print "Checked item: [item]".
    If the loop finishes without finding a valid email, return None
"""

from typing import Any

def find_first_valid_email(emails: list[Any]) -> str | None:
    """
    Returns the first valid email or None if no email found

    Args:
        emails: list[Any]

    Returns:
        str|None
    """
    for item in emails:
        try:
        
            if '@' in item and isinstance(item,str)  :
                print("Valid email found!")
                return item
            continue
        except TypeError as te:
            print(f"Error, {te}")
        finally:
            print(f"Checked item : {item}")

emails1 = ["test", None, "user@example.com", "another@domain.net"]
found_email = find_first_valid_email(emails1)
print(f"email found : {found_email}")
# Expected: Prints "Checked item: test", "Skipping non-string item: None", 
#          "Checked item: None", "Checked item: user@example.com", 
#          "Valid email found!", "Checked item: user@example.com" (finally runs!), 
#          Returns "user@example.com"

emails2 = ["no_at_sign", "also_no_at", None, 123]
found_email = find_first_valid_email(emails2)
print(f"email found : {found_email}")
# Expected: Prints checked/skipped messages for all, returns None