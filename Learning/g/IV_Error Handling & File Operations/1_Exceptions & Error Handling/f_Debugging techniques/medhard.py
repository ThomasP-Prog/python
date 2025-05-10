"""
Problem: The get_top_students function is likely returning an empty list or crashing with a TypeError instead of ['Alice', 'Charlie']. 
Describe how you would use print debugging or a conceptual debugger to inspect the values of name, avg, 
and threshold right before the if statement inside the loop executes, to diagnose why the comparison is failing.
"""

def get_top_students(average_grades_dict, threshold):
    top_students = []
    for name, avg in average_grades_dict.items():
        print(f"name in for : {name}")
         # Bug: Should be name >= threshold
        print(f"name type : {type(name)}")
        print(f"threshold type : {type(threshold)}")
        print(f"is name and threshold of same type : {type(name) == type(threshold)}")
        if name >= threshold: # Incorrectly compares name (str) with threshold (float)
            print("in if")
            top_students.append(name)
        print("after if")
    print("after for")
    return top_students

avg_grades = {'Alice': 91.0, 'Bob': 75.5, 'Charlie': 88.0}
passing_threshold = 80.0
top = get_top_students(avg_grades, passing_threshold)
print(top) # Might produce unexpected results or TypeError