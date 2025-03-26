def get_score() -> int:
    """Prompt user to enter score and validate."""
    while True:
        try:
            score = round(float(input("Enter your score : ").strip()))
            if score >= 0 and score <= 100:
                return int(score)
            else:
                print("Score need to be between 0 and 100 included")
        except ValueError:
            print("Score has to be a number.")
        except KeyboardInterrupt:
            print("You exited the program.")
            exit()

def grade_score(score : int) -> None:
    """Print letter grade of the score."""
    if score >= 0 and score <= 100:
        if score >= 90:
            print(f"Your score : {score} | Grade : A")
        elif score >= 80:
            print(f"Your score : {score} | Grade : B")
        elif score >= 70:
            print(f"Your score : {score} | Grade : C")
        elif score >= 60:
            print(f"Your score : {score} | Grade : D")
        else:
            print(f"Your score : {score} | Grade : F")

def main() -> None:
    score = get_score()
    grade_score(score)

if __name__ == "__main__":
    main()