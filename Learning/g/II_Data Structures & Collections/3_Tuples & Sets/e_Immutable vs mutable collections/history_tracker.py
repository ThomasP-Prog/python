"""Create a Python class HistoryTracker that stores a mutable list of states. 
   Implement methods add_state(new_state) and undo(). 
   The challenge is how to store the new_state data: if the states themselves are mutable objects 
   (e.g., dictionaries representing application state), how do you ensure that adding a new state
   or undoing doesn't cause unexpected modifications to previous states stored in the history 
   list due to shared mutable object references? Demonstrate the problem and implement a solution (likely involving copying)."""

import copy

class HistoryTracker:
    """ Stores a list of states"""    
    def __init__(self,initial_state : dict):
        """ Class initialisation"""
        self.tracker = [copy.deepcopy(initial_state)]
    
    def add_state(self,new_state : dict):
        """ Add a new state"""
        safe_copy = copy.deepcopy(new_state)
        self.tracker.append(safe_copy)

    def undo(self):
        """ Reverts to the previous state by removing the current state"""
        if len(self.tracker) > 1:
            self.tracker.pop()
        else:
            print("Can't undo intial state")

    def get_current_state(self) -> dict:
        """Return a deep copy of the current state"""
        if not self.tracker:
            return {}
        return copy.deepcopy(self.tracker[-1])


def main() -> None:
    """main function"""

    initial_state = {
        'document_id': 'doc1',
        'content': ['Line 1', 'Line 2'],
        'editors': {'alice'} 
    }

    state_after_edit_1 = {
        'document_id': 'doc1',
        'content': ['Line 1 - edited', 'Line 2', 'Line 3 added'], # Changed list
        'editors': {'alice', 'bob'} # Changed set
    }

    state_after_edit_2 = {
        'document_id': 'doc1',
        'content': ['Line 1 - edited', 'Line 2', 'Line 3 added'], # Same content as previous state
        'editors': {'alice', 'bob', 'charlie'} # Changed set
    }

    tracker = HistoryTracker(initial_state)
    print(tracker.get_current_state())
    tracker.add_state(state_after_edit_1)
    print(tracker.get_current_state())
    tracker.add_state(state_after_edit_2)
    print(tracker.get_current_state())
    tracker.undo()
    print(tracker.get_current_state())

if __name__ == "__main__":
    main()