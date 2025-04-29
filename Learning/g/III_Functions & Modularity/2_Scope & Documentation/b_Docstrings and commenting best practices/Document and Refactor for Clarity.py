"""Refactor slightly for readability (better names, maybe intermediate steps), and:
    - Add a comprehensive docstring,
    - Write clear inline comments explaining:
        - Scoring logic,
        - Bonus conditions,
        - Final adjustment/cap logic,
    - Add basic error handling (optional, depending on what you’ve covered)."""

# Function to calculate final score with potential bonus
def calc_final(points : int|float, bonus_flag : bool):
    """
    Calculate final score depending on the points and if the bonus flag is True

    Args:
        points : current points
        bonus_flag : bool - is the bonus applied ?

    Returns:
        final score
    """
    # Check input types (basic error handling example)
    if not isinstance(points, (int, float)) or not isinstance(bonus_flag, bool):
         raise ValueError("Error: Invalid input types.")

    # Base calculation
    final_score = points * 1.1 # Apply some base multiplier

    if bonus_flag:
        # Apply bonus points of 15 if bonus_flag is True and final_score > 50
        if final_score > 50:
            final_score = final_score + 15 # Add bonus points
        # Apply bonus points of 5 if bonus_flag is True and final_score <= 50
        if final_score <= 50:
            final_score = final_score + 5

    # Put final_score to 100 if cap is reached
    if final_score > 100:
        final_score = 100 # Cap the score at 100

    return final_score

def main() -> None:
    """main function"""
    try:
        points=40
        bonus_flag=True #→ Final Score: 49
        final_score = calc_final(points,bonus_flag)
        print(final_score)
        points=60
        bonus_flag=True #→ Final Score: 81
        final_score = calc_final(points,bonus_flag)
        print(final_score)
        points=95
        bonus_flag=False #→ Final Score: 100
        final_score = calc_final(points,bonus_flag)
        print(final_score)
        points=95
        bonus_flag=True #→ Final Score: 100
        final_score = calc_final(points,bonus_flag)
        print(final_score)
        points="abc"
        bonus_flag=True #→ Expected: None or error message
        final_score = calc_final(points,bonus_flag)
        print(final_score)
    except ValueError as v:
        print(v)

if __name__ == "__main__":
    main()