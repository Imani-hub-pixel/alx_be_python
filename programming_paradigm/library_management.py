class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title=title
        self.author=author
        self.___is_checked_out=_is_checked_out
    def check_out_book(self):
        return self.___is_checked_out
    def return_book(self):
        self.___is_checked_out=False
        return self.___is_checked_out

        
class Library(Book):
    def __init__(self):
        self.___books=[]
    def add_book(self,title):
        self.___books.append(title)
    def check_out_book(self,title):
        self.___books.append(title)
    def return_book(self,title):
        self.___books.append(title)
    def list_available_books(self):
        return self.___books