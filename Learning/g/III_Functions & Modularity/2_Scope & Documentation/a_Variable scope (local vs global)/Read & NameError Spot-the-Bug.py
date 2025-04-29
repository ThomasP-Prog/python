game_name = "Space Invaders"

def print_game(game:str) -> None:
    """
    print the name of the game

    Args:
        game : name of the game

    Returns:
        print the name of the game
    """
    if not game:
        raise ValueError("Game name must be a non-empty string")

    print(f"The game is {game}")
    message = "Let's play "+game_name
    print(message)

def main() -> None:
    """main function"""
    print_game(game_name)
    message = "defining to hide error in IDE" # defining to hide error in IDE
    try:
        print(message) #not define outside the function
    except NameError as n:
        print(f"Error printing : {n}")

if __name__ == "__main__":
    main()
