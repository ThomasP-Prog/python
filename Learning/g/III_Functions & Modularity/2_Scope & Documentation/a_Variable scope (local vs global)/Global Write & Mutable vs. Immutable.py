score = 0
moves = []

def increase_score() -> None:
    """
    Increase score by one
    """
    try:
        score += 1
    except UnboundLocalError as u:
        print(f"Error : {u}")
        print("Calling fixed function")
        fixed_increased()

def fixed_increased() -> None:
    """Fixing increase_score"""
    global score
    score +=1

def log_move(m : str) -> None:
    """
    add m to the log

    Args:
        m : string
    """
    if not isinstance(m,str):
        raise TypeError("'m' must be a string")

    moves.append(m)

def main() -> None:
    """main function"""
    print(score)
    increase_score() # causes UnboundLocalError
    print(score)

    for move in ["one", "two", "three"]:
        log_move(move)
        print(f" After log_move('{move}') →", moves)


if __name__ =="__main__":
    main()