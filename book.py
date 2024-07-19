class Book:
    def __init__(self, title, author, isbn,publication_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__is_borrowed = False
    # getters and setters
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publication_date(self):
        return self.__publication_date
    
    def get_genre(self):
        return self.__genre
    
    def is_borrowed(self):
        return self.__is_borrowed
    
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False
    
    def return_books(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False
    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.isbn}, Published: {self.__publication_date}, Genre: {self.__genre}, Genre:{self.__genre}, Borrowed: {self.__is_borrowed} "

        
        

