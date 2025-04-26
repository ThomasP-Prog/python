import datetime

def get_year() -> int:
    """prompt user year of birth, validate and return it"""
    while True:
        try:
            year = int(input("year of birth : "))
            if year > datetime.date.today().year:
                print("year is in the futre, insert year")
            else:
                return year
        except ValueError:
            print("insert year :")

def age_calcul(age) -> int:
    """calcul age based on age of birth"""
    return datetime.date.today().year - age

def main():
    year = get_year()
    print(f"year of birth : {year}, age : {age_calcul(year)}")

if __name__ == "__main__":
    main()