"""You are given a list of tuples representing friendship relationships in a social network: 
   (user_id1, user_id2). Write a function create_friend_graph that takes this list as input and returns a dictionary. 
   The keys of the dictionary should be user IDs, and the values should be sets containing the IDs of that user's friends. 
   After creating the dictionary, iterate through each user and print their friend list."""



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


if __name__ == "__main__":
    main()