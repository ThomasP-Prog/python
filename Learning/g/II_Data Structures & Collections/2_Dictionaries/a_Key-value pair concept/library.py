import datetime

def get_input(prompt : str,data_type : type = str) -> str|int:
    """Prompt user to enter an inout and validate"""
    while True:
        try:
            new_input = input(f"Enter {prompt} : ").strip()
            if not new_input:
                raise ValueError
            if data_type in [int]:
                if new_input.isdigit():
                    return int(new_input)
            return new_input
        except ValueError:
            print(f"Error. {prompt} can't be empty")

def new_book(library : dict) -> dict:
    """Add a new book to the library"""
    title = get_input("title")
    author = get_input("author")
    library[len(library)+1] = {
        "title" : title,
        "author" : author,
        "borrower_name": None,
        "date_borrowed": None,
        "borrow_counter": 0
    }
    print("New book added.")
    return library

def return_book(library : dict) -> dict:
    """return a book to the library"""
    id = get_input("book ID",int)
    if id not in library:
        print("Error. Book ID not found.")
        return library
    if library[id]["borrower_name"] != None and library[id]["date_borrowed"] != None:
        library[id]["borrower_name"] = None
        library[id]["date_borrowed"] = None
        print("Book returned")
    else:
        print("Error. Book not currently borrowed.")
    return library

def borrow_book(library : dict) -> dict:
    """Borrow a book from the library"""
    id = get_input("book ID",int)
    if id not in library:
        print("Error. Book ID not found.")
        return library
    if library[id]["borrower_name"] == None and library[id]["date_borrowed"] == None:
        borrower = get_input("borrowed name")
        library[id]["borrower_name"] = borrower
        library[id]["date_borrowed"] = datetime.date.today()
        library[id]["borrow_counter"] += 1
        print("Book borrowed")
    else:
        print("Error. Book currently borrowed.")
    return library

def most_borrowed(library : dict) -> None:
    """print most borrowed books"""
    sorted_books = sorted(library.items(), key=lambda x: x[1]["borrow_counter"], reverse=True)
    max_books = min(10,len(sorted_books))
    print("-" * 50)
    print(f"Top {max_books} borrowed books :")
    print("-" * 50)
    x = 0
    for i in range(max_books):
        book = sorted_books[i]
        print(f"{book[1]['title']} by {book[1]['author']} - borrowed {book[1]['borrow_counter']} times")

def list_by_author(library : dict) -> None:
    """print books by author"""
    print("-" * 50)
    print("Books by author :")
    print("-" * 50)
    author = get_input("name of author")
    books = [library[book_id]["title"] for book_id in library if library[book_id]["author"] == author]
    if not books:
        print(f"No books by author {author}")
    else:
        print(f"Books by {author}:")
        for book in books:
            print(f"- {book}")

def currently_borrowed(library : dict) -> None:
    """print currently borrowed books"""
    books = [library[book_id]["title"] for book_id in library if library[book_id]["borrower_name"] != None]
    if not books:
        print(f"No books are currently borrowed.")
    else:
        print("-" * 50)
        print(f"Borrowed books :")
        print("-" * 50)
        for book in books:
            print(f"- {book}")

def main() -> None:
    """main function"""
    library = {
    1: {"title": "1984", "author": "George Orwell", "borrower_name": None, "date_borrowed": None, "borrow_counter": 5},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "borrower_name": None, "date_borrowed": None, "borrow_counter": 3},
    3: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "borrower_name": None, "date_borrowed": None, "borrow_counter": 7},
    4: {"title": "Moby Dick", "author": "Herman Melville", "borrower_name": None, "date_borrowed": None, "borrow_counter": 2},
    5: {"title": "War and Peace", "author": "Leo Tolstoy", "borrower_name": None, "date_borrowed": None, "borrow_counter": 4},
    6: {"title": "Pride and Prejudice", "author": "Jane Austen", "borrower_name": None, "date_borrowed": None, "borrow_counter": 6},
    7: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "borrower_name": None, "date_borrowed": None, "borrow_counter": 8},
    8: {"title": "Brave New World", "author": "Aldous Huxley", "borrower_name": None, "date_borrowed": None, "borrow_counter": 1},
    9: {"title": "The Hobbit", "author": "J.R.R. Tolkien", "borrower_name": None, "date_borrowed": None, "borrow_counter": 9},
    10: {"title": "Fahrenheit 451", "author": "Ray Bradbury", "borrower_name": None, "date_borrowed": None, "borrow_counter": 5},
    11: {"title": "Jane Eyre", "author": "Charlotte Brontë", "borrower_name": None, "date_borrowed": None, "borrow_counter": 3},
    12: {"title": "The Odyssey", "author": "Homer", "borrower_name": None, "date_borrowed": None, "borrow_counter": 2},
    13: {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "borrower_name": None, "date_borrowed": None, "borrow_counter": 4},
    14: {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "borrower_name": None, "date_borrowed": None, "borrow_counter": 10},
    15: {"title": "The Divine Comedy", "author": "Dante Alighieri", "borrower_name": None, "date_borrowed": None, "borrow_counter": 1},
    16: {"title": "Frankenstein", "author": "Mary Shelley", "borrower_name": None, "date_borrowed": None, "borrow_counter": 2},
    17: {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "borrower_name": None, "date_borrowed": None, "borrow_counter": 3},
    18: {"title": "A Tale of Two Cities", "author": "Charles Dickens", "borrower_name": None, "date_borrowed": None, "borrow_counter": 6},
    19: {"title": "Les Misérables", "author": "Victor Hugo", "borrower_name": None, "date_borrowed": None, "borrow_counter": 4},
    20: {"title": "Dracula", "author": "Bram Stoker", "borrower_name": None, "date_borrowed": None, "borrow_counter": 2},
}
    library = new_book(library)
    print(library)
    library = borrow_book(library)
    print(library)
    library = return_book(library)
    print(library)
    most_borrowed(library)
    list_by_author(library)
    currently_borrowed(library)

if __name__ =="__main__":
    main()
