"""Create a function that takes a list of words and returns a dictionary
   where the keys are the words and the values are their lengths.
   Then modify it to count how many times each word appears in the list."""

from collections import Counter

def word_length(words : list) -> dict:
    """Count length of each words"""
    lenght = {}
    if words:
        for word in words:
            if word not in lenght:
                lenght[word] = len(word)
    else:    
        print("List if empty.")
    return lenght

def word_frequency(words : list) -> dict:
    """Count frequency of words in a list"""
    return dict(Counter(word for word in words if word))

def print_words_length(length : dict) -> None:
    """Print words length"""
    if not length:
        return
    words = sorted(length.items(),key=lambda x: x[1], reverse = True)
    print("Words length :")
    print("_"*30)
    for word,leng in words:
        print(f"{word} : {leng} letters")

def print_word_frequency(freq : dict) -> None:
    """Print frequency of words"""
    if not freq:
        return
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse = True) # sort words with frequency
    print("Word frequency :")
    print("_"*30)
    for word,count in sorted_words:
        print(f"{word} : {count} occurrences")

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
    words = [word.lower().strip(',.!?:;()[]"\'') for word in text.split()] # make a list out of the string without punctuation
    freq = word_frequency(words)
    print_word_frequency(freq)
    leng = word_length(words)
    print_words_length(leng)


if __name__ == "__main__":
    main()
