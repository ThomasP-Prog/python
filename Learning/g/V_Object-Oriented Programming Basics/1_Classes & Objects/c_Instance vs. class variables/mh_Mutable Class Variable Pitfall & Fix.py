"""
Define a class Team. Add a class variable default_members = [] (a list).
In its __init__, take team_name (string). Add an instance attribute self.members and initialize it by assigning Team.default_members to it.
Add a method add_member(member_name: str) that appends member_name to self.members.
Add a method list_members() that prints the team name and its members.
Demonstrate the Problem: Create two Team instances (team_a, team_b). 
Add a member to team_a. List members for both team_a and team_b. 
Observe that the member was added to both (because they share the same default_members list object).
Fix the Problem: Modify the Team class's __init__ method so that each team gets its own independent list of members, 
correctly initialized if default_members were meant as an initial template (e.g., self.members = list(Team.default_members) 
or self.members = Team.default_members.copy(), or more simply, if default members aren't meant to be a starting template, just self.members = []). 
Demonstrate that after the fix, adding a member to one team does not affect the other.
"""

class Team:
    default_members = []
    def __init__(self,team_name:str) -> None:
        """Initialize the team"""
        self.name = team_name
        # self.members = Team.default_members doesn't work
        self.members = list(Team.default_members) # does

    def add_member(self,member_name:str) -> None:
        """Add a member to the team"""
        self.members.append(member_name)

    def list_members(self) -> None:
        """Print the list of member"""
        if not self.members:
            print(f"Team {self.name} is empty")
        else:
            print(f"Team {self.name} :")
            for member in self.members:
                print(member)

def main() -> None:
    """main function"""
    team1 = Team("Rocket")
    team2 = Team("Bot")
    team1.add_member("Jessie")
    team1.list_members()
    team2.list_members()

if __name__ == "__main__":
    main()

        