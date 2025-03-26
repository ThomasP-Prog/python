import re

def longest_word(paragraph :str) -> None:
    """Print longest word with the number of letters"""
    words = re.findall(r"\b[\w'-]+\b",paragraph)
    if not words:
        print("N ovalide words found")
        return
    
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    print(f"Longest word(s) : {', '.join(longest_words)} with {max_length} letters")

def main() -> None:
    """main function"""
    #hard entry of paragraph for to not have to type it
    paragraph = "Python is a powerful and versatile programming language known for its simplicity and readability. It is widely used in web development, data science, automation, artificial intelligence, and more. With its vast ecosystem of libraries and frameworks, Python enables developers to write efficient and scalable code for various applications."
    longest_word(paragraph)

if __name__ == "__main__":
    main()