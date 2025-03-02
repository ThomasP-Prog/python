def account_balance() -> int:
    while True:
        try:
            balance = (float(input("what's your balance ? ")))
            if balance < 0:
                print("Balance cannot be negative.")
                continue
            if not balance.is_integer():
                print("Please enter a whole number.")
                continue
            return int(balance)
        except ValueError:
            print("Wrong number")

def withdrawal() -> int:
    while True:
        try:
            withdraw = float(input("Enter withdrawal amount :"))
            if withdraw <= 0:
                print("Withdrawal amount must be greater than 0.")
                continue
            if not withdraw.is_integer():
                print("Please enter a whole number.")
                continue
            return int(withdraw)
        except ValueError:
            print("wrong amount")

def approval(balance: int, withdraw : int) -> bool:
    if withdraw%10 == 0:
        if balance >= withdraw:
            print("Success")
            return True
        else:
            print("Insufficient balance")
            return False
    else:
        print("Withdraw must be multiple of 10")
        return False
    
def main() -> None:
    balance = account_balance()
    withdraw = withdrawal()
    approved = approval(balance,withdraw)

if __name__ == "__main__":
    main()