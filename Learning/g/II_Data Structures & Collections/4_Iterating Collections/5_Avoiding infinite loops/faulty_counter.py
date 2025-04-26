"""You are given a function that is supposed to simulate charging a battery to 100%. 
   However, it contains a logic error leading to an infinite loop. 
   Identify the error and fix the function so it correctly prints charging messages and stops at 100%.

   Concepts Reinforced: while loop condition, variable updates, comparison operators."""


def charge_battery():
    """simulate charging of a battery"""
    charge_level = 10
    print("Starting charge...")
    while charge_level < 100:
        print(f"Charge level: {charge_level}%")
        charge_level += 5
        if charge_level > 100:
            charge_level = 100
    print(f"Charge level: {charge_level}%")
    
    print("Battery fully charged.")

def main() -> None:
    """main function"""
    charge_battery()

if __name__ == "__main__":
     main()
