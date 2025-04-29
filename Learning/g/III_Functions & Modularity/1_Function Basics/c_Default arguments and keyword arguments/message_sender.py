"""Define a function send_message that takes message_text (required) and optional configuration parameters: 
   recipient (string, default "support@example.com"), sender (string, default "noreply@example.com"), 
   and encrypt (boolean, default False). The function should simulate sending the message by printing the details, 
   formatted like: "Sending message: '[message_text]' | From: [sender] | To: [recipient] | Encrypted: [True/False]". 
   Call the function multiple times using keyword arguments to change the recipient, sender, or encryption status.

   Concepts Reinforced: Multiple default arguments (string, boolean), keyword arguments for clarity, 
   calling with overridden defaults, string formatting with multiple variables."""


def send_message(message_text:str,recipient:str="support@example.com",sender:str="noreply@example.com",encrypt:bool=False) -> None:
    """
    Simulate the sending of a message according to arguments

    Args:
        message_text : message
        recipient : recipient of the message
        sender : sender of the message
        encrypt : check is the message is encrypted
    
    Returns:
        Print the formatted message
    """
    print(f"Sending message : '{message_text}' | From : {sender} | To : {recipient} | Encrypted : {encrypt}")

def main() -> None:
    """main function"""
    send_message("System reboot required.")
    send_message("Meeting updated.", recipient="team@example.com")
    send_message("Confidential report attached.", encrypt=True, recipient="manager@example.com")
    send_message("Server status OK", sender="monitor@example.com", recipient="admin@example.com")

if __name__ == "__main__":
    main()