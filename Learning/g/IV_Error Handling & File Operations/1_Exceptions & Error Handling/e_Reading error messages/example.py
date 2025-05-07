# --- Code that causes an error ---
def calculate_average(numbers_list):
    print(f"Calculating average for: {numbers_list}")
    total = sum(numbers_list)
    count = len(numbers_list)
    # Potential ZeroDivisionError if numbers_list is empty
    average = total / count  
    return average

def analyze_data(data):
    # Assume data is {'scores': []}
    scores = data['scores'] # Potential KeyError if 'scores' key is missing
    avg = calculate_average(scores) # Potential ZeroDivisionError if scores is empty
    print(f"Average score: {avg}")

# --- Main execution ---
student_data = {'name': 'Test User', 'scores': []} # Empty list will cause ZeroDivisionError

# We wrap in try/except here ONLY to simulate printing the traceback neatly
#try:
analyze_data(student_data)
'''except ZeroDivisionError as e:
    print("\n--- SIMULATED TRACEBACK OUTPUT ---")
    print("Traceback (most recent call last):")
    # 1. The initial call in the script (e.g., line 20 in your_script.py)
    print('  File "your_script.py", line 20, in <module>')
    print('    analyze_data(student_data)')
    # 2. The call inside analyze_data (e.g., line 15 in your_script.py)
    print('  File "your_script.py", line 15, in analyze_data')
    print('    avg = calculate_average(scores)')
    # 3. The call inside calculate_average where the error *actually* happened (e.g., line 8)
    print('  File "your_script.py", line 8, in calculate_average')
    print('    average = total / count')
    # 4. The Exception Type and Message
    print(f"ZeroDivisionError: division by zero") 
    print("--- END OF SIMULATED TRACEBACK ---")'''