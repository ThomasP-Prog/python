visit_count = 0

def bump() -> None:
    """Increment visit_count by 1"""
    global visit_count
    visit_count += 1

def report() -> None:
    """Shadow visit_count locally and print both"""
    visit_count = -1
    print(f"Local visit count : {visit_count}")
    print(f"Global still {globals().get('visit_count','Not defined')}")

def counter(count=[0]):
    count[0] += 1
    return count[0]

def main() -> None:
    """main function"""
    
    for i in range(5):   
        print(counter())
        #bump()
    #report()
    print(counter)
if __name__ == "__main__":
    main()