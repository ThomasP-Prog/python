def get_withdrawal_amount() -> int:
    """Prompt user to enter the withdraw amount and validate"""
    while True:
        try:
            withdraw = input("Enter withdraw number :").strip()
            if not withdraw.replace('.','',1).isdigit(): # Check if the user input (withdraw) is a valid numeric value, including integers and floating-point numbers.
                                                         # Replace 1st occurence of '.', 1 = only 1 dot removed
                print("Invalid input. Enter a whole number multiple of 10€.")
                continue
            withdraw = float(withdraw)
            if withdraw.is_integer():
                withdraw = int(withdraw)
                if withdraw%10 == 0 and withdraw > 0:
                    return withdraw
                else:
                    print("Withdraw need to be positive multiple of 10€.")
            else:
                print("Withdrawal must be a whole number.")
        except KeyboardInterrupt:
            print("Transaction canceled. goodbye.")
            exit()

def process_withdrawal(balance : int, withdraw : int) -> int:
    """check if balance is sufficient and execute withraw"""
    if balance >= withdraw:
        balance -= withdraw
        print(f"Withdrawing {withdraw}€ from balance {balance}€")
        print(f"Balance : {balance}€")
        return balance
    else:
        print("Balance insufficient.")
        return balance
            

def main() -> None:
    balance = 5000
    while True:  # Keep retrying until a valid withdrawal is made
        withdraw = get_withdrawal_amount()
        new_balance = process_withdrawal(balance, withdraw)
        if new_balance != balance:  # Only update if withdrawal succeeded
            balance = new_balance
            break  # Exit loop after a successful withdrawal

if __name__ == "__main__":
    main()