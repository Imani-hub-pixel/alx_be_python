class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title=title
        self.author=author
        self.__is_checked_out=_is_checked_out
    def check_out_book(self):
        self.__is_checked_out
    def return_book(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True   # checkout successful
        return False  
        
class Library(Book):
    def __init__(self):
        self.__books=[]
    def add_book(self,title):
        self.__books.append(title)
    def check_out_book(self,title):
        self.__books.append(title)
    def return_book(self,title):
        self.__books.append(title)
    def list_available_books(self):
        return self.__books