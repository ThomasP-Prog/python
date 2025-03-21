import tkinter as tk
from tkinter import ttk
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        
        # Result variable and display
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create display frame
        self.display_frame = tk.Frame(root, height=50, bg="#e6e6e6")
        self.display_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create display entry
        self.display = tk.Entry(
            self.display_frame, 
            textvariable=self.result_var,
            font=('Arial', 24),
            bd=0,
            bg="#e6e6e6",
            justify="right"
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create buttons frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure button grid
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)
        self.buttons_frame.columnconfigure(3, weight=1)
        
        # Button data (text, row, column, colspan)
        self.buttons = [
            ('C', 0, 0, 1), ('⌫', 0, 1, 1), ('%', 0, 2, 1), ('/', 0, 3, 1),
            ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
            ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
            ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
            ('0', 4, 0, 2), ('.', 4, 2, 1), ('=', 4, 3, 1)
        ]
        
        # Create buttons
        for (text, row, col, colspan) in self.buttons:
            self.create_button(text, row, col, colspan)
            
        # Initialize variables
        self.current_expression = "0"
        self.last_operation = None
    
    def create_button(self, text, row, col, colspan):
        # Define button style based on text
        style = 'TButton'
        
        # Create button
        button = ttk.Button(
            self.buttons_frame, 
            text=text, 
            style=style,
            command=lambda t=text: self.button_click(t)
        )
        
        # Position button
        button.grid(row=row, column=col, columnspan=colspan, sticky=tk.NSEW, padx=2, pady=2)
        
        # Configure row weight to make buttons expand
        self.buttons_frame.rowconfigure(row, weight=1)
    
    def button_click(self, text):
        if text == 'C':
            self.clear()
        elif text == '⌫':
            self.backspace()
        elif text == '=':
            self.calculate()
        elif text in ['+', '-', '*', '/', '%']:
            self.add_operator(text)
        elif text == '.':
            self.add_decimal()
        else:
            self.add_digit(text)
            
        # Update display
        self.update_display()
    
    def clear(self):
        self.current_expression = "0"
    
    def backspace(self):
        if len(self.current_expression) == 1 or self.current_expression == "Error":
            self.current_expression = "0"
        else:
            self.current_expression = self.current_expression[:-1]
    
    def add_digit(self, digit):
        if self.current_expression == "0" or self.current_expression == "Error":
            self.current_expression = digit
        else:
            self.current_expression += digit
    
    def add_decimal(self):
        # Check if we already have a decimal in the last number
        parts = re.split(r'[+\-*/]', self.current_expression)
        if '.' not in parts[-1]:
            self.current_expression += '.'
    
    def add_operator(self, operator):
        # Check if the expression ends with an operator
        if self.current_expression[-1] in ['+', '-', '*', '/']:
            self.current_expression = self.current_expression[:-1] + operator
        else:
            self.current_expression += operator
    
    def calculate(self):
        try:
            # Replace % with /100 before evaluation
            expression = self.current_expression.replace('%', '/100')
            
            # Evaluate expression
            result = eval(expression)
            
            # Format result (handle long float results)
            if isinstance(result, float):
                # If result is a whole number, convert to int
                if result.is_integer():
                    result = int(result)
                # If result has many decimal places, format it
                elif len(str(result)) > 10:
                    result = round(result, 8)
            
            self.current_expression = str(result)
        except Exception:
            self.current_expression = "Error"
    
    def update_display(self):
        self.result_var.set(self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()