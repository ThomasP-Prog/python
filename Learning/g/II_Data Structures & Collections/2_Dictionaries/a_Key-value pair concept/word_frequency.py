def get_answer() -> bool:
    """Prompt user if they want to remove common words"""
    while True:
        try:
            answer = input("do you want to remove common words (the,a,is,and) ? yes / no : ").strip()
            if answer == "yes":
                return True
            elif answer == "no":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Error. Enter yes or no.")


def word_frequency(text : str, remove : bool) -> dict:
    """Count frequency of each words in a text"""
    common = ["the","a","is","and"]
    freq = {}
    words = [word.lower().strip(',.!?:;()[]"\'') for word in text.split()]
    
    for word in words:
        if word and (not remove or word not in common):
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                
    return freq

def print_count(freq: dict) -> None:
    """Print frequency of each words in a text"""
    print("Frequency of words:")
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    """Sorts the dictionary items by values (x[1] refers to the second element in the tuple).
       Sorts in descending order (highest value first)."""
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main() -> None:
    """main function"""
    text = "Python is a powerful, high-level programming language known for its simplicity," \
    " readability, and versatility, making it one of the most widely used languages in fields" \
    " such as web development, data science, artificial intelligence, automation, and software" \
    " development. With its clean syntax and vast ecosystem of libraries, Python enables developers" \
    " to write efficient and maintainable code with fewer lines compared to other languages like C++" \
    " or Java. Its extensive standard library and third-party packages, such as NumPy for numerical" \
    " computing, Pandas for data analysis, and TensorFlow for machine learning, make it a top choice" \
    " for both beginners and professionals. Additionally, Python's strong community support and" \
    " open-source nature contribute to its continuous evolution, ensuring that it remains a leading" \
    " language for solving complex problems in various domains."
    freq = {}
    remove_common = get_answer()
    freq = word_frequency(text,remove_common)
    print_count(freq)

if __name__ == "__main__":
    main()