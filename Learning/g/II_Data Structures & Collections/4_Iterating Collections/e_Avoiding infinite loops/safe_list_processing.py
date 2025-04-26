"""Write a function process_until_negative(data_list) that processes numbers from a list. 
   It should iterate through the list using a while loop and an index. For each number, print its value. 
   The loop should stop immediately if it encounters a negative number OR if it runs out of items in the list. 
   Ensure the loop cannot become infinite, even with an empty list or a list containing only non-negative numbers. 
   Return the number of items processed before stopping (or hitting the end).

   Concepts Reinforced: while loop with compound condition (and), list indexing, checking list bounds, variable updates, returning a value."""

def process_until_negative(data_list : list[int]) -> int:
    """Counts non-negative numbers from start until first negative or end"""
    if not data_list:
        return 0
    
    count = 0
    i = 0

    while i < len(data_list):
        if data_list[i] < 0:
            break
        count +=1
        i +=1
    return count


def main() -> None:
    """main function"""
    list1 = [10, 25, 30, -5, 15, 20] # Should stop at -5, process 3 items
    print(process_until_negative(list1))
    list2 = [100, 200, 300]          # Should stop at the end, process 3 items
    print(process_until_negative(list2))
    list3 = []                       # Should stop immediately, process 0 items
    print(process_until_negative(list3))
    list4 = [-10, 20, 30]             # Should stop at -10, process 0 items
    print(process_until_negative(list4))
    # Expected Outputs (Return Values): 3, 3, 0, 0

if __name__ == "__main__":
    main()