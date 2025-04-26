"""Create a function that models group memberships. 
   It should take a dictionary where keys are group names and values are sets of member IDs. 
   The function should also take two group names (group_a, group_b). 
   Return a dictionary summarizing their relationship: 
   {'common': set_of_common_members, 'a_only': set_of_members_only_in_a, 'b_only': set_of_members_only_in_b}"""

def is_in_group(group_a : set[str],group_b : set[str]) -> dict[str,set[str]]:
    """Compares two sets and finds common and unique elements."""
    if not group_a or not group_b:
        return dict()
    
    common = group_a & group_b
    a_only = group_a - group_b
    b_only = group_b - group_a

    group_dict = {
        "common" : common,
        "a_only" : a_only,
        "b_only" : b_only
    }
    return group_dict

def print_group(groups : dict[str,set[str]]) -> None:
    """Format who is in which group"""
    if not groups:
        return
    
    for group, members in groups.items():
        print(f"Group : {group}")
        print(f"{', '.join(str(member) for member in members)}")
        print("-"*15)

def main() -> None:
    """main function"""

    group_memberships = {
    "group_a": {"u001", "u002", "u003", "u004"},
    "group_b": {"u003", "u005", "u006"}
}
    group_dict = is_in_group(group_memberships["group_a"],group_memberships["group_b"])
    print_group(group_dict)


if __name__ == "__main__":
    main()