"""
Define a class Robot (use pass in its body for now). Write a function deploy_robots(count: int) -> list. 
This function should take an integer count. 
Inside the function, use a loop to create count number of Robot instances and append each new instance to a list. 
The function should return this list of Robot instances. In your main function, call deploy_robots with a number (e.g., 5) 
and print the length of the returned list and the type of the first element in the list.
Sample Data: Call deploy_robots(5).
"""
from typing import List

class Robot:
    pass

def deploy_robots(count: int) -> List[Robot]:
    """
    Make a list with 'count' amount of Robot

    Args:
        count : int

    Returns:
        List[Robot]
    """
    robot_list = []
    for _ in range(count):
        robot_list.append(Robot())

    return robot_list

def main() -> None:
    """main function"""
    robot_list = deploy_robots(5)
    print(f"Robot list lenght : {len(robot_list)}")
    if robot_list:
        print(f"Type of first element of robot list : {type(robot_list[0])}")
    else:
        print("Robot list is empty")

if __name__ == "__main__":
    main()