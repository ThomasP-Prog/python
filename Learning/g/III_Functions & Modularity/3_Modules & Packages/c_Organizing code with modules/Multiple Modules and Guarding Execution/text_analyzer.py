"""Describe text_analyzer.py: Contains functions:
   - count_words(text: str) -> int: Returns the number of words in the text (simple split by space).
   - count_chars(text: str, include_spaces: bool = True) -> int: Returns the number of characters (optionally excluding spaces).
   - Include an if __name__ == "__main__": block in this file that demonstrates these functions with a sample text string and 
   prints the results only when text_analyzer.py is run directly."""

def count_words(text : str) -> int:
    """
    Count the number of words in a string

    Args:
        text : str
    
    Returns:
        int
    """
    return len(text.split())

def count_chars(text : str, include_spaces : bool = True) -> int:
    """
    Count the number of words in a string

    Args:
        text : str
    
    Returns:
        int
    """
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ",""))

def main() -> None:
    """main function"""

    sample_doc = "This is a sample document."
    print(f"--- Testing text_analyzer.py directly ---")
    print(f"Sample Text: '{sample_doc}'")
    print(f"{count_words(sample_doc)}")
    print(f"{count_chars(sample_doc)}")


if __name__ == "__main__":
    main()