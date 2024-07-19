import re
from library import Library

def validate_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu")
    print("1. Book Operation")
    print("2. User Operation")
    print("3. Author Operation")
    print("4. Genre Operation")
    print("5. Quit")
    return validate_input("Select an option:", r"^[1-5]$")

def book_operations(library):
    while True:
        print("\nBook Operation:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book ")
        print("Search for a book")
        print("Display all books")
        print("Back to main Menu")
        choice = validate_input("Select an option: ", r"^[1-6]$")
        if choice == '1':
            title = input("Enter book title:")
            author = input("Enter author title:")
            isbn = input("Enter isbn title:")
            publication_date = input("Enter book title:")
            genre =  input("Enter genre title:")
            library.add_book(title, author, isbn, publication_date, genre)
            print("Book added successfully.")
        elif choice == '2':
            book_id = input("Enter book ISBN or title to borrow:")
            user_id =  input("Enter your library ID:")
            if library.borrow_book(book_id, user_id):
                print("Book borrowed successfully")
            else:
                print("Book borrowing failed. Either the book is not availbale or user ID is invalid.")
        elif choice == '3':
            book_id = input("Enter book ISBN or title to return:")
            user_id = input("Enter your library ID:")
            if library.return_book(book_id, user_id):
                print("Book returned successfully.")
            else:
                print("Book return failed. Either the book was not borrowed or user ID is invalid.")
        elif choice == '4':
            book_id = input("Enter book ISBN or title to search:")
            book = library.find_book(book_id)
            if book:
                print(book)
            else:
                print("Book not found.")
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            break

def user_operations(library):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("Back to main menu")
        choice = validate_input("Select an option: ", r"^[1-4]$")
        if choice == '1':
            name = input("Enter user name:")
            library_id = input("Enter library_ID:")
            library.add_user(name, library_id)
            print("User added successfully.")
        elif choice == '2':
            user_id = input("Enter user library ID to view details:")
            user = library.find_user(user_id)
            if user:
                print(user)
            else:
                print("User not found.")
        elif choice == '3':
            library.display_users()
        elif choice == '4':
            break

def author_operations(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all author")
        print("Back to main menu")
        choice = validate_input("Select an option: ", r"^[1-4]$")
        if choice == '1':
            name = input("Enter author name:")
            biography = input("Enter biography:")
            library.add_author(name, biography)
            print("Author added successfully.")
        elif choice == '2':
            author_name  = input("Enter author name to view details:")
            for author in library.authors:
                if author.get_name().lower() == author_name.lower():
                    print(author)
                    break
                else:
                    print("Author not found")
        elif choice == '3':
            library.display_authors()
        elif choice == '4':
            break

def genre_operations(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all author")
        print("Back to main menu")
        choice = validate_input("Select an option: ", r"^[1-4]$")
        if choice == '1':
            name = input("Enter genre name:")
            description = input("Enter description:")
            category = input("Enter category:")
            library.add_genre(name, description, category)
            print("Genre added successfully.")
        elif choice == '2':
            genre_name  = input("Enter genre name to view details:")
            for genre in library.genres:
                if genre.get_name().lower() == genre_name.lower():
                    print(genre)
                    break
                else:
                    print("Genre not found")
        elif choice == '3':
            library.display_genres()
        elif choice == '4':
            break
if __name__ == "__main__":

    library = Library()
    while True:
        choice = main_menu()
        if choice == '1':
            book_operations(library)
        elif choice == '2':
            user_operations(library)
        elif choice == '3':
            author_operations(library)
        elif choice == '4':
            genre_operations(library)
        elif choice == '5':
         print("Exiting the Library Managment System.")
        


 








            










