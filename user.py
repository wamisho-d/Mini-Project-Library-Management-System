class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

# getters and setters
def get_name(self):
    return self.__name

def get_library_id(self):
    return self.__library_id

def borrow_book(self, book_title):
    self.__borrowed_books.append(book_title)

def return_book(self, book_title):
    if book_title in self.__borrowed_books:
        self.__borrowed_books.remove(book_title)

def get_borrowed_books(self):
    return self.__borrowed_books

def __str__(self):
    return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {','.join(self.__borrowed_books)}"

