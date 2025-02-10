# i have to create a one class library , 2 variable must 1.no. of books 2. list of books
# in this we have to add books get no. of books and show all books in library also persistance of data

class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
        
    def showInfo(self):
        print(f"Library has a {self.no_of_books} books.\nBooks are:")
        for book in self.books:
            print(book)
            
obj1=Library()
obj1.add_book("Python")
obj1.add_book("Java")
obj1.add_book("C++")
obj1.add_book("C")
obj1.add_book("C#")
Library.showInfo(obj1)
obj1.showInfo()       