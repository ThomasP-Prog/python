"""Write a function that takes a list of email addresses (strings).
   The function should return a tuple containing two sets:
   the first set should contain all valid email addresses from the list,
   and the second set should contain all invalid email addresses.
   Define "valid" for this exercise as containing exactly one "@" symbol
   and at least one "." symbol after the "@". (This is a simplified validation rule)."""

import re

def check_email(emails : list[str]) -> tuple[set[str],set[str]]:
    """Check if email is valid then return valid and invalid ones separetly """
    if not emails:
        return set(), set()
    
    valid_emails = set()
    invalid_emails = set()

    # Correct email formatting
    correct_format = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    for email in emails:
        if re.fullmatch(correct_format,email):
            valid_emails.add(email)
        else:
            invalid_emails.add(email)
    return valid_emails,invalid_emails

def print_checked_emails(checked_emails : set[str],valid : bool = True) -> None:
    """Print emails that have been checked"""
    if not checked_emails:
        return
    
    if valid:
        print("Valid emails :")
    else:
        print("Invalid emails :")
    
    print("-"*15)
    for email in checked_emails:
        print(email)


def main() -> None:
    """main function"""
    emails = [
    "john.doe@gmail.com",
    "alice123yahoo.com",
    "mike@outlookcom",
    "susan@.com",
    "tom.hanks@",
    "jane.doe@hotmailcom",
    "noah@company.",
    "chris@@gmail.com",
    "linda@mail.server.com",
    "emma.gmail.com"
]
    valid_emails,invalid_emails = check_email(emails)
    print_checked_emails(valid_emails)
    print_checked_emails(invalid_emails,False)

if __name__ == "__main__":
    main()