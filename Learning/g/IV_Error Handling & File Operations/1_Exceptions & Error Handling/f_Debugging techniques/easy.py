"""
Problem: Calling check_sign(0) produces no output. How would you use print() statements inside the function to figure out why?
"""

def check_sign(number):
    print(f"Condition (number > 0) is: {number > 0}")
    if number > 0:
       print("Inside the if block")
       print("Positive") 
    print("Finished if check")
    # Bug: Missing check for zero/negative
    # else: <--- imagine this else block is missing
    #    print("Zero or Negative") 
check_sign(0) # Prints nothing, but should print "Zero or Negative"