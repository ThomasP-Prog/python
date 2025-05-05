def process_list(items):
    total = 0
    for i in range(len(items)): # Potential issue if items isn't a sequence
         try:
             total += items[i].value # Potential issues here
         except TypeError: # Catching TypeError, but what causes it?
             print("Type error processing item") 
    return total

data1 = [{'value': 5}, {'value': 10}] 
# What is printed/returned for process_list(data1)?

data2 = [{'value': 5}, None]
# What exception might occur *inside* the loop for process_list(data2)? 
# (Consider accessing .value on None)

data3 = 123
# What exception might occur *before* the loop for process_list(data3)?
