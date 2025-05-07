"""
Problem: find_item(my_items, "banana") incorrectly returns -1. Describe how you would use print() statements 
inside the loop or use a conceptual debugger (breakpoints, stepping, inspecting) to see the values being compared 
in the if statement on each iteration and identify the logical error.
"""

def find_item(items_list, item_to_find):
    found_index = -1 # Default if not found
    for i in range(len(items_list)):
        print(f"item inside loop : {i}")
        # Bug: Compares index `i` instead of element `items_list[i]`
        print(f"condition i == item_to_find is {i == item_to_find}")
        if i == item_to_find: 
            print("inside if")
            found_index = i
            # Missing break here adds inefficiency but isn't the main bug
        print("if finished")
    print("for finished")
    return found_index

my_items = ["apple", "banana", "cherry"]
index = find_item(my_items, "banana") # Returns -1, but should return 1
print(index)