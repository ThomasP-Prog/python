"""Write a function that takes a list of sets (list_of_sets). 
   Find all elements that are present in at least one set but not present in all sets. 
   Return these elements as a single set. (Hint: Think about the union of all sets and the intersection of all sets)."""

def elements_not_in_all(sets_list : list[set[str]]) -> set[str]:
    """Find unique element in a list of set"""
    if not sets_list:
        return set()
    
    # Calculate Union of ALL sets
    # Method 1: Using update in a loop
    overall_union = set()
    for s in sets_list:
        overall_union.update(s)
    # Method 2: Using functools.reduce (more advanced)
    # overall_union = functools.reduce(lambda a, b: a | b, sets_list)

    if sets_list: # Check again in case list had only empty sets etc.
         overall_intersection = sets_list[0].copy() 
         for i in range(1, len(sets_list)):
             overall_intersection.intersection_update(sets_list[i]) # Use intersection_update
         # Method 2: Using functools.reduce (more advanced)
         # overall_intersection = functools.reduce(lambda a, b: a & b, sets_list)
    else:
         overall_intersection = set()

    # Calculate the difference (Union - Intersection)
    result = overall_union - overall_intersection
    return result
        
def print_unique(elements : set[str]) -> None:
    """Format print of unique elements"""
    print(f"Unique elements : {', '.join(str(element) for element in elements)}")

def main() -> None:
    """main function"""
    sets_list = [
    {"python", "sql", "java"},           # Set 0
    {"cloud", "python", "sql"},          # Set 1
    {"python","c++", "javascript", "java"},       # Set 2
    {"python", "java", "cloud", "sql"},  # Set 3
    {"python","javascript", "html", "css"},       # Set 4
    {"python","sql", "cloud"},                    # Set 5
    {"java", "python", "cloud"},         # Set 6
    {"python","c#", "sql", "cloud", "java"},      # Set 7
    {"html", "css", "python"},           # Set 8
    {"python","java", "c++", "cloud"}             # Set 9
]
    elements = elements_not_in_all(sets_list)
    print_unique(elements)
if __name__ == "__main__":
    main()