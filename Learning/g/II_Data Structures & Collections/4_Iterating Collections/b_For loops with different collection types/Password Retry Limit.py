"""Simulate a simple password check. Define a correct password (e.g., "python123") 
   and a maximum number of attempts (e.g., 3). Use a while loop that continues as long 
   as the number of attempts made is less than the maximum and the entered password is not correct. 
   Inside the loop, prompt the user for the password, increment the attempt counter. 
   After the loop, check if the password was entered correctly or if the attempts ran out, 
   and print an appropriate message ("Access granted" or "Access denied")."""

def password_check(password : str) -> None:
    """Check if user enter the right password with attempts"""
    attempt = 1
    max_attempt = 3
    access_granted = False

    while attempt <= max_attempt :
        guess = input(f"Attempt {attempt}/{max_attempt} - Enter password : ").strip()
        if guess == password:
            access_granted = True
            break

        attempt += 1
    if access_granted == True:
        print("Access granted")
    else:
        print("Access denied")


def main() -> None:
    """main function"""
    password = "python123"
    password_check(password)

if __name__ == "__main__":
    main()