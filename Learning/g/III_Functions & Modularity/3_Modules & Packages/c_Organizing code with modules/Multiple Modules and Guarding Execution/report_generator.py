"""
Describe report_generator.py: Imports the text_analyzer module (using an alias like ta). 
Contains a function generate_summary(title: str, document_text: str) -> str 
that uses the functions from text_analyzer (e.g., ta.count_words(), ta.count_chars()) 
to create a summary string like: "Report: [title]\nWord Count: [count]\nCharacter Count (incl. spaces): [count]"
   """

import text_analyzer as ta

def generate_summary(title : str, text : str) -> str:

    word_count = ta.count_words(text)
    char_count = ta.count_chars(text)

    return f"Report: {title}\nWord Count: {word_count}\nCharacter Count (incl. spaces): {char_count}"