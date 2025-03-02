def newPerson(name :str,age :int,height :float)->dict:
    """Create and return dictionary"""
    return {
        "name" : name,
        "age" : age,
        "height" : height
    }

def displayPerson(person :dict) -> None:
    """Format and print"""
    print(f"Age : {person['name']}, Age : {person['age']}, Height : {person['height']}m")

def main():
    name = "thomas"
    age = 30
    height = 1.85
    person = newPerson(name,age,height)
    displayPerson(person)
if __name__ == "__main__":
    main()