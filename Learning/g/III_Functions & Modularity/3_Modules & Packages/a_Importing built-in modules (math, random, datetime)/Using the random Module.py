"""Import the random module. Create a list of at least 5 different color names (strings). 
   First, use random.randint() to generate a random integer representing the number of picks 
   (num_picks) between 1 and 3 (inclusive). Then, print a message indicating how many colors will be picked. 
   Finally, use random.choice() inside a for loop that runs num_picks times; inside the loop, 
   pick and print a random color from your list on each iteration (prefixing it with "- ")"""


import random

def main() -> None:
    """main function"""

    colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
    num_picks = random.randint(1,3)

    if num_picks == 1:
        print(f"{num_picks} color will be picked")
    else:
        print(f"{num_picks} colors will be picked")

    for _ in range(0,num_picks):
        print(f"- {random.choice(colors)}")

if __name__ == "__main__":
    main()
