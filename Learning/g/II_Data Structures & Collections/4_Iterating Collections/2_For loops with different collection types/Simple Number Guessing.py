"""Write a program where you define a secret number (e.g., secret = 7). 
   Use a while loop to repeatedly ask the user to guess the number. If the guess is wrong, 
   tell them if their guess was too high or too low. The loop should continue while the guess 
   is not equal to the secret number. When they guess correctly, print a congratulatory message and exit the loop."""

def find_number(secret : int) -> None:
    """ask user for number into they find the right one"""
    if not secret or not isinstance(secret,int):
        return
    
    guess = float('inf')

    while guess != secret:
        try:
            guess = input("Guess the number : ").strip()
            guess = int(guess)
            if guess > secret:
                print("Too high !")
            if guess < secret:
                print("Too low !")
            
            
        except ValueError:
            print("The guess as to be a whole number")

    print("Congratulations! You guessed it!")

def main() -> None:
    """main function"""
    secret = 7
    find_number(secret)



if __name__ == "__main__":
    main()
