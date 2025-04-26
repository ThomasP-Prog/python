def print_first_last(cities : list) -> None:
    print(f"The first city is {cities[0]}")
    print(f"The last city is {cities[-1]}")

def replace_second_city(cities : list) -> None:
    if len(cities) > 1:
        cities[1] = "Budapest"

def add_new_city(cities : list) -> None:
    cities.append("Milan")

def main() -> None:
    cities_list = ["Paris","London","Berlin","Madrid","Rome"]
    print(cities_list)
    print_first_last(cities_list)
    replace_second_city(cities_list)
    print(cities_list)
    add_new_city(cities_list)
    print(cities_list)


if __name__ == "__main__":
    main()