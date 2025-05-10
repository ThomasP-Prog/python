"""
Assume you have an input file scores.txt where each line contains a player's name and score separated by a comma (e.g., "Alice,85"). 
Write a function generate_report(input_filename: str, output_filename: str, threshold: int). This function should:
    - Read the input_filename line by line using with open().
    - For each line, parse the name (string) and score (integer). Use try...except ValueError (and potentially IndexError if splitting fails) 
    to handle lines that might be malformed (e.g., missing comma, score not a number). Print a warning for skipped lines.
    - Keep track of valid scores.
    - Calculate the average score of valid entries.
    - Write a report to output_filename using with open() in write mode ('w'). The report should contain:
        - Line 1: "Score Report"
        - Line 2: "Average Score: [average]" (formatted to 2 decimal places)
        - Line 3: "Players Above Threshold ([threshold]):"
        - Subsequent lines: List the names of players whose valid score was strictly greater than the threshold.
    - Handle FileNotFoundError for the input file.
"""

from pathlib import Path

def generate_report(input_filename: str, output_filename: str, threshold: int) -> None:
    """
    Read from input file and generate a report

    Args:
        input_filename: str
        output_filename: str
        threshold: int

    Returns:
        None
    """
    script_directory = Path(__file__).parent
    input_full_path = script_directory / input_filename
    output_full_path = script_directory / output_filename
    total = 0
    count = 0
    player_dict = dict()
    try:
        print(f"--- Attempting to read {input_filename} ---")
        with open(input_full_path,mode='r',encoding='utf-8') as infile:
            for line in infile:
                try:
                    new_line = line.split(',')
                    name = new_line[0]
                    score = int(new_line[1])
                    player_dict[name] = score
                    total += score
                    count += 1
                except (IndexError,ValueError) as e:
                    print(f"Warning: Skipping malformed line: '{line.strip()}'. Error: {e}")
        print("--- Reading Successful ---")

        if count == 0:
            print("No valid score")
            average = 0.0
        else:
            average = total / count

        print(f"--- Attempting to write {output_filename} ---")
        with open(output_full_path,mode='w',encoding='utf-8') as outfile:
            outfile.write("Score Report :\n")
            outfile.write(f"Average Score: {average}\n")
            outfile.write(f"Players Above Threshold ({threshold}) :\n")
            for player,score in player_dict.items():
                if score > threshold:
                    outfile.write(f"{player}\n")
        print("--- Writing Successful ---")

    except (FileNotFoundError,Exception) as e:
        print(f"Error, {e}")
    
def main() -> None:
    """main function"""
    generate_report('score.txt', 'report.txt', 90)


if __name__ == "__main__":
    main()
    # Expected content of 'report.txt':
    # Score Report
    # Average Score: 87.60 # Avg of 85, 92, 78, 95, 88
    # Players Above Threshold (90):
    # Bob
    # Eve
    # (Warnings about "David,invalid" and "Frank," would be printed to console)