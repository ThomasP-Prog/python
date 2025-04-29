"""Define a function log_event(event_type, *details, **metadata) that takes a required event_type (string), 
   any number of positional details (e.g., specific data points), and any keyword metadata 
   (e.g., timestamp="2025-04-28", user_id=123). The function should print the event type, then each detail, 
   and finally each metadata key-value pair"""

from typing import Any

def log_event(event_type : str, *details : Any, **metadata : Any) -> None:
    """
    log event from event_type, arguments and keyword arguments

    Args :
        event_type : type of event
        *details : arbitrary argument
        **metadata : arbitrary keyword argument

    Returns:
        None
    """
    print(f"Event Type : {event_type}")
    if details:
        for detail_item in details:
            print(f"Detail: {detail_item}")
    for data,value in metadata.items():
        print(f"Metadata : {data} = {value}")

def main() -> None:

    log_event("FILE_ACCESS", "Read operation", "file: /data/report.txt", user="admin", time="17:10")
    # Expected Output:
    # Event Type: FILE_ACCESS
    # Detail: Read operation
    # Detail: file: /data/report.txt
    # Metadata: user = admin
    # Metadata: time = 17:10

    log_event("NETWORK_ERROR", "Connection timeout", server="192.168.1.100")
    # Expected Output:
    # Event Type: NETWORK_ERROR
    # Detail: Connection timeout
    # Metadata: server = 192.168.1.100

    log_event("STARTUP")
    # Expected Output:
    # Event Type: STARTUP

if __name__ == "__main__":
    main()