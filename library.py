from book import Book
from user import User
from author import Author
from genre import Genre

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

# Book Operations
def add_book(self, title, author, isbn, publication_date, genre):
    new_book = Book(title, author, isbn, publication_date, genre)
    self.books.append(new_book)

def find_book(self, identifier):
    for book in self.books: 
        if book.get_isbn() == identifier or book.get_title().lower() == identifier.lower():
            return book
        return None
    
def borrow_book(self, identifier, user_id):
    book = self.find_book(identifier)
    user = self.find_user(user_id)
    if book and user and not book.is_borrowed():
        book.borrow()
        user.borrow_book(book.get_title)
        return True
    return False

def return_book(self, identifier, user_id):
    book = self.find_book(identifier)
    user = self.find_user(user_id)
    if book and user and book.is_borrowed():
        book.return_book()
        user.return_book(book.get_title())
        return True
    return False

def display_books(self):
    for book in self.books:
        print(book)

# user operations
def add_user(self, name, library_id):
    new_user = User(name, library_id)
    self.user.append(new_user)

def find_user(self, user_id):
    for user in self.users:
        if user.get_library_id() == user_id:
            return user
        return None

def dispaly_users(self):
    for user in self.users:
        print(user)

# Author Operations

def add_author(self, name, biography):
    new_author = Author(name, biography)
    self.author.append(new_author)

def dispaly_authors(self):
    for author in self.authors:
        print(author)

# Genre Operation
def add_genre(self, name, description, category):
    new_genre = Genre(name, description, category)
    self.genre.append(new_genre)

def dispaly_genres(self):
    for genre in self.genres:
        print(genre)


    





    
