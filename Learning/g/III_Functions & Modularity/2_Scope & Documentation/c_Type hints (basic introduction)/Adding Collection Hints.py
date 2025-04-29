"""Take your solution code for the exercise group_users_by_location (from the previous section). 
   Add appropriate type hints using the typing module (List, Tuple, Dict, Set) to the function signature 
   (parameters and return value) and key variables."""


from typing import Mapping, List, Tuple, Set,Dict

def group_users_by_location(checkins_data: List[Tuple[str, str]]) -> Mapping[str, Set[str]]:
    """
    Return groups of users by location
    
    Args:
        checkins_data: List[Tuple[str, str]])
    
    Returns:
        Mapping[str, Set[str]]
    """
    groups_by_location : Dict[str, Set[str]] = {}
    for user,location in checkins_data:
        groups_by_location.setdefault(location,set()).add(user)

    return groups_by_location

def print_groups(groups: Mapping[str, Set[str]]) -> None:
    """Format groups by location"""
    if not groups:
        return
    print("Groups by user location :")
    print("-"*25)
    for group,users in groups.items():
        print(f"{group} : {sorted(users)}")


def main() -> None:
    """main function"""

    checkins_data = [
        ("user1", "locA"),
        ("user2", "locB"),
        ("user1", "locB"), # user1 checks into locB again
        ("user3", "locA"),
        ("user2", "locB"), # user2 checks into locB again
        ("user1", "locA"), # user1 checks into locA again
        ("user4", "locC"),
        ("user3", "locA"), # user3 checks into locA again
    ]
    groups = (group_users_by_location(checkins_data))
    print_groups(groups)

if __name__ == "__main__":
    main()