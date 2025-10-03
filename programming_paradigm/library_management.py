class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title=title
        self.author=author
        self.___is_checked_out=_is_checked_out
        
class Library(Book):
    def __init__(self):
        self.___books=[]
    def add_book(self,title):
        self.___books.append(title)
        return not self.___is_checked_out
    def check_out_book(self,title):
        self.___books.append(title)
        return self.___is_checked_out
    def return_book(self,title):
        self.___books.append(title)
        return not self.___is_checked_out
    def list_available_books(self):
        return self.___books