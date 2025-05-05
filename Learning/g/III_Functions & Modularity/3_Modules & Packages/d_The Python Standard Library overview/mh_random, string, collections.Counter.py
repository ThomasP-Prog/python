"""
Write a function analyze_random_text(num_chars: int) -> dict. 
Generate a random string of lowercase letters (string.ascii_lowercase) 
with the specified num_chars length using random.choices (or random.choice in a loop). 
Then, analyze this random string to count the frequency of each letter. 
Return a dictionary where keys are the letters that appeared in the string and values are their counts
"""

import random
import string
import collections
from typing import Dict

def analyze_random_text(num_chars: int) -> Dict[str,int]:
    """
    Returns a dict of char : occurence based on number of char

    Args :
        num_chars: int

    Returns:
        Dict[str,int]
    """
    if num_chars <= 0:
        return {}

    random_char : list[str] = random.choices(string.ascii_lowercase,k=num_chars)
    
    char_counts = collections.Counter(random_char)
    char_counts = sorted(char_counts.items())
    
    return dict(char_counts)


def main() -> None:
    """main function"""

# Example call:
    frequency = analyze_random_text(1000)
    print(frequency) 
# Expected output: A dictionary like {'a': 45, 'b': 38, ..., 'z': 41} 
# (Counts will vary due to randomness)
# You can implement the counting with a standard dictionary or look up
# `collections.Counter` which is specialized for this.

if __name__ == "__main__":
    main()