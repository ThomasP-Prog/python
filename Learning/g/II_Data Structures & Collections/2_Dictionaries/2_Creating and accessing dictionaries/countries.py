def get_country() -> str:
    """Prompt user to enter a country"""
    while True:
        try:
            country = input("Which country do you want to know the capital : ").strip().title()
            if not country :
                raise ValueError
            return country
        except ValueError:
            print("Error. Country name can't be empty.")

def print_capital(countries : dict) -> None:
    """Print capital asked by user"""
    country = get_country()
    if country in countries:
        capital = countries[country]["capital"]
        print(f"The capital of {country} is {capital}")
    else:
        print(f"{country} not in the list")

def main() -> None:
    """Main function"""
    countries = {
        'France' :{'capital' : 'Paris', 'population' : 1000000,'languages' : ['français']},
        'Germany' :{'capital' : 'Berlin', 'population' : 2000000,'languages' : ['german','english']},
        'UK' :{'capital' : 'London', 'population' : 10000000,'languages' : ['german','english','français']},
        'Spain' :{'capital' : 'Madrid', 'population' : 600000,'languages' : ['Spanish']},
        'Italy' :{'capital' : 'Rome', 'population' : 800000,'languages' : ['Italian']}
        }
    print_capital(countries)

if __name__ == "__main__":
    main()
    