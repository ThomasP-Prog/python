"""You are given a list of tuples representing friendship relationships in a social network: 
   (user_id1, user_id2). Write a function create_friend_graph that takes this list as input and returns a dictionary. 
   The keys of the dictionary should be user IDs, and the values should be sets containing the IDs of that user's friends. 
   After creating the dictionary, iterate through each user and print their friend list."""

from collections import defaultdict

def create_friend_graph(friendships : list[tuple[str, str]]) -> dict[str, set[str]]:
    """Return dict of friendship list"""
    if not friendships:
        print("Input dict is empty")
        return dict()
    
    friendships_dict = defaultdict(set)
    
    for pair in friendships:
        if not isinstance(pair, tuple) or len(pair) != 2:
            continue
        
        user1, user2 = pair

        if not isinstance(user1, str):
            print(f"Warning: Skipping pair {pair} - user '{user1}' is not a string.")
            continue
        if not isinstance(user2, str):
             print(f"Warning: Skipping pair {pair} - user '{user2}' is not a string.")
             continue
        
        
        friendships_dict[user1].add(user2)
        friendships_dict[user2].add(user1)

    return friendships_dict

def print_friendship(friendships_dict : dict[str, set[str]]) -> None:
    """Format frienship dict"""
    for user,friends in friendships_dict.items():
        print(f"{user}'s friends : {friends}")

def main() -> None:

    friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "David"),
    ("David", "Eve"),
    ("Alice", "David"), # Alice is friends with David too
    ]
# Expected output (printed):
# Alice's friends: {'Bob', 'Charlie', 'David'}  # Order of set may vary
# Bob's friends: {'Alice', 'David'}
# Charlie's friends: {'Alice', 'David'}
# David's friends: {'Bob', 'Charlie', 'Alice', 'Eve'}
# Eve's friends: {'David'}
    friendships_dict = create_friend_graph(friendships)
    print_friendship(friendships_dict)

if __name__ == "__main__":
    main()