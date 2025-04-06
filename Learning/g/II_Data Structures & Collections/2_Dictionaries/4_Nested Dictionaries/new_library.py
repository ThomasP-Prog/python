from datetime import datetime
import re
def get_string(prompt : str, string_type : str) -> str:
    while True:
        try:
            new_string = input(prompt).strip()

            if string_type == "title" or string_type == "author":
                if new_string.replace(" ","").replace("'","").replace("-","").isalpha():
                    return new_string
                else:
                    raise ValueError
            elif string_type == "status":
                if new_string == "available" or new_string == "check out":
                    return new_string
                else:
                    raise ValueError
            else:
                print("Error. Missing string type")
                exit()
        except ValueError:
            if string_type == "status":
                print("Error. Enter 'available' or 'check out'")
            else:
                print(f"Error. {string_type.capitalize} can't be a number or contain special character other then ' and - ")

def get_int(prompt : str, int_type : str) -> int:
    while True:
        try:
            new_int = int(input(prompt).strip())

            if int_type == "year":
                if new_int > 700 and new_int <= datetime.now().year and isinstance(new_int, int):
                    return int(new_int)
                else:
                    raise ValueError
            elif int_type == "copies":
                if new_int >= 0 and new_int <= 10 and isinstance(new_int, int):
                    return int(new_int)
                else:
                    raise ValueError
            else:
                print("Error. Missing int type")
                exit()
        except ValueError:
            if int_type == "year":
                print(f"Error. Enter a year between 700 and {datetime.now().year}")
            else:
                print(f"Error. Enter a number between 1 and 10")

def add_book(library : dict, section : str) -> dict:
    if section and library:
        print("Adding a new book.")
        title = get_string("Enter book title : ","title")
        author = get_string("Enter book author : ","author")
        year = get_int("Enter book year : ","year")
        copies = get_int("Enter number of copies : ","copies")
        if copies > 0:
            status = "available"
        else:
            status = "checked out"

        library[section][len(library[section])] = {
            "title": title,
            "author": author,
            "year": year,
            "status": status,
            "copies": copies
        }
        print("Book added.")
        return library

def update_book(library : dict, section : str, id : int) -> dict:
    if library and section and id in range(0,len(library[section])):
        changes = 9
        while changes != 0:
            print(f"{library[section][id]}")
            print("Enter 1 to change title")
            print("Enter 2 to change author")
            print("Enter 3 to change year")
            print("Enter 4 to change number if copies")
            print("Enter 0 to apply changes")
            changes = int(input().strip())

            if changes == 1:
                title = get_string("Change book title : ","title")
                library[section][id]["title"] = title
            elif changes == 2:
                author = get_string("Change book author : ","author")
                library[section][id]["author"] = author
            elif changes == 3:
                year = get_int("Change book year : ","year")
                library[section][id]["year"] = year
            elif changes == 4:
                copies = get_int("Change number of copies : ","copies")
                library[section][id]["copies"] = copies
                if copies > 0:
                    library[section][id]["status"] = "available"
                else:
                    library[section][id]["status"] = "checked out"
    else:
        print("Error. Missing argument")
    return library

def remove_book(library : dict, section : str, id : int) -> dict:
    if library and section and id in range(0,len(library[section])):
           del library[section][id]
           print("Book removed.")
    else:
        print("Error. Missing argument")
    return library
    
def search_book(library : dict, author_name : str) -> dict:
    result = {}
    if library and author_name:
        for section, books in library.items():
            for book_id,book_data in books.items():
                if book_data['author'] == author_name:
                    result[book_id] = book_data
    return result

def multi_criteria_search(library : dict, **criteria) -> dict:
    result = {}
    if library and criteria:
        for section in library.values():
            for book_id, book_data in section.items():
                if all(book_data.get(key) == value for key, value in criteria.items()):
                    full_id = f"{section}_{book_id}"
                    result[full_id] = book_data
    return result

def date_range_search(library : dict, min_year, max_year) -> dict:
    if library and min_year and max_year:
        result = {}
        for section, books in library.items():
            for book_id, book_data in books.items():
                if book_data["year"] >= min_year and book_data["year"] <= max_year:
                    full_id = f"{section}_{book_id}"
                    result[full_id] = book_data
    return result

def criteria_search(library : dict, criteria : str) -> dict:
    result = {}
    if library and criteria:
        pattern = rf"\b[\w\s]*{criteria}[\w\s]*\b"
        for section, books in library.items():
            for book_id, book_data in books.items():
                found_title = re.findall(pattern.lower(),book_data['title'].lower())
                found_author = re.findall(pattern.lower(),book_data['author'].lower())
                if found_title or found_author:
                    full_id = f"{section}_{book_id}"
                    result[full_id] = book_data
    return result

def available_books(library : dict) -> None:
    if library:
        current_section = None
        for section, books in library.items():
            if current_section != section:
                print(f"Available {section} books :")
                current_section = section
            for book_id, book_data in books.items():
                if book_data.get('status') ==  "available":
                    print(book_data['title'])

    if not library:
        print("Library is empty.")
        return
        
    section_counts = {}
    section_available = {}
    total_books = 0
    total_available = 0
    
    # Count books in each section
    for section_name, books in library.items():
        section_counts[section_name] = 0
        section_available[section_name] = 0
        
        for book_data in books.values():
            copies = book_data.get('copies', 0)
            section_counts[section_name] += copies
            total_books += copies
            
            if book_data.get('status') == 'available':
                section_available[section_name] += copies
                total_available += copies
    
    # Display statistics
    print("\nLIBRARY STATISTICS:")
    print("-" * 60)
    print(f"Total books in collection: {total_books}")
    print(f"Total available books: {total_available} ({total_available/total_books*100:.1f}% of collection)")
    print("\nBooks by section:")
    
    for section, count in section_counts.items():
        if total_books > 0:
            percentage = count / total_books * 100
            print(f"- {section}: {count} books ({percentage:.1f}% of collection)")
    
    print("\nAvailability by section:")
    for section, count in section_available.items():
        if section_counts[section] > 0:
            availability = count / section_counts[section] * 100
            print(f"- {section}: {count}/{section_counts[section]} available ({availability:.1f}%)")
    print("-" * 60)



def main() -> None:
    library = {
    "Fiction": {
        0: {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "status": "available",
            "copies": 3
        },
        1: {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "status": "checked out",
            "copies": 0
        },
        2: {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "status": "available",
            "copies": 2
        }
    },
    "Non-Fiction": {
        0: {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "year": 2011,
            "status": "available",
            "copies": 4
        },
        1: {
            "title": "Educated",
            "author": "Tara Westover",
            "year": 2018,
            "status": "available",
            "copies": 6
        }
    },
    "Reference": {
        0: {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "year": 1988,
            "status": "checked out",
            "copies": 0
        },
        1: {
            "title": "The Selfish Gene",
            "author": "Stephen Hawking",
            "year": 1976,
            "status": "available",
            "copies": 2
        }
    }
}
    #library = add_book(library, "Fiction")
    #library = update_book(library,"Fiction",0)
    #remove_book(library,"Fiction",0)
    #result = search_book(library,"Stephen Hawking")
    #result = criteria_search(library,"ing")
    #result = multi_criteria_search(library, author = "Stephen Hawking", status = "available")
    #result = date_range_search(library, 1900, 2000)
    available_books(library)
    
if __name__ == "__main__":
    main()