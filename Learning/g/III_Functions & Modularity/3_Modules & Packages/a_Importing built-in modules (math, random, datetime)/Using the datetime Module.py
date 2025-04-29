"""Import the datetime module (you can use an alias like dt). Get the current date using datetime.date.today(). 
   Print the current date formatted exactly as MM/DD/YYYY (e.g., "04/29/2025"). 
   You'll need to use the strftime method and find the correct format codes.
"""

import datetime as dt # Using an alias is optional

def main() -> None:
    """main function"""
    today_date = dt.date.today()
    formatted_date = today_date.strftime("%m/%d/%Y")
    print(f"Today's date is: {formatted_date}")

if __name__ == "__main__":
    main()