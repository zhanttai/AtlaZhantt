class Book:
    title: str
    __author: str
    pages: int
    is_read: bool

book.Book = Book("Дюна", "Фрэнк Герберт", 412)

def __init__ (self, title, author, pages, is_read):
    self.title = title 
    self.author = author
    self.pages = pages
    self.is_read = False 

def mark_as_read(self, status):
    self.is_read = True
    status = ("Прочитана")

def short_info(self, title, author, pages, is_read):
    if self.is_read == True:
        
    print (title, author, pages, is_read, sep="|")


