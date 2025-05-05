"""
Write a function format_event_schedule(events: list[tuple[str, str]]) -> list[str]. 
The input is a list of tuples, where each tuple contains an event name (string) and 
an event start time as an ISO format string (e.g., "YYYY-MM-DDTHH:MM:SS"). 
Use the datetime.datetime.fromisoformat() method to parse the string into a datetime object. 
Format each event into a string like "Event: [Event Name] starts on 
[Weekday Name], [Month Name] [Day], [Year] at [HH:MM AM/PM]". Return a list of these formatted strings
"""

from datetime import datetime

def format_event_schedule(events: list[tuple[str, str]]) -> list[str]:
    """
    format the event shedule in a list

    Args:
        events : list[tuple[str, str]]
    
    Returns:
        list[str]
    """
    new_list = []
    for event,date in events:
        date = datetime.fromisoformat(date)
        formatted_date = date.strftime("%A, %B %d, %Y at %I:%M %p")
        new_string = f"{event} starts on {formatted_date}"
        new_list.append(new_string)
    return new_list

def print_events(event_list : list[str]) -> None:
    """
    print event list
    
    Args:
        event_list : list[str]

    Returns:
        print
    """
    if not event_list:
        print("No event")
        return
    
    print("Events :")
    for event in event_list:
        print(event)
    
def main() -> None:
    """main function"""
    event_data = [
        ("Meeting", "2025-05-15T14:00:00"),
        ("Workshop", "2025-05-16T09:30:00"),
        ("Conference Call", "2025-05-15T10:00:00")
    ]
    event_list = format_event_schedule(event_data)
    print_events(event_list)
    # Example Expected Output element: 
    # "Event: Meeting starts on Thursday, May 15, 2025 at 02:00 PM" 
    # (Use strftime formatting codes for weekday, month, day, year, hour, minute, AM/PM)

if __name__ == "__main__":
    main()