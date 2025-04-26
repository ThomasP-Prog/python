"""Write a function summarize_valid_transactions(transactions: list[dict]) -> dict. 
   The input is a list of transaction dictionaries. Each dictionary might have keys 'id' (str), 
   'amount' (float), and 'status' (str). The function should iterate through the transactions. 
   Use continue to skip any transaction where the 'status' is not equal to 'completed' OR the 
   'amount' is less than or equal to 0. For valid transactions ('completed' status, positive amount), 
   calculate the total amount and count the number of valid transactions. 
   Return a dictionary summarizing the results, e.g., {'total_amount': 150.75, 'count': 3}"""

def summarize_valid_transactions(transactions: list[dict]) -> dict:
    """Calculate total of valid transaction and their number"""
    if not transactions:
        return dict()
    
    total = 0
    count = 0

    for trans in transactions:
        amount = trans.get("amount",0)
        status = trans.get("status","")
        if amount <= 0 or status != "completed":
            continue
        
        total += amount
        count += 1
    return {"total_amount" : total,
            "count" : count}


def main() -> None:
    """main function"""

transactions_data = [
    {'id': 'a', 'amount': 100.50, 'status': 'completed'},
    {'id': 'b', 'amount': -20.00, 'status': 'completed'}, # Invalid amount
    {'id': 'c', 'amount': 50.25, 'status': 'pending'},    # Invalid status
    {'id': 'd', 'amount': 75.00, 'status': 'completed'},
    {'id': 'e', 'amount': 0.00, 'status': 'completed'},   # Invalid amount
    {'id': 'f', 'amount': 25.00, 'status': 'completed'},
]
summary = summarize_valid_transactions(transactions_data)
print(summary)
# Expected output: {'total_amount': 200.75, 'count': 3}

if __name__ == "__main__":
    main()