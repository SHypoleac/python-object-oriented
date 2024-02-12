# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods
def checkisinstance(self, other):
    if not isinstance(other, Book):
        raise TypeError("You cannot compare two objects of different types")
        
class Book:
    books=[]
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        books.append(self)
        
    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
        checkisinstance(self, other)
        return (self.title == other.title and self.author == other.author)
    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, other):
        checkisinstance(self, other)
        return (self.price >= other.price)

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
        checkisinstance(self, other)
        return (self.price < other.price)
    
    def __str__(self):
        return (f"{self.title}")

    def showbooks():
        for book in books:
            print book


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print("is b1 is equalto b3 :",b1==b3)
print("Is b1 equal to b2 :",b1==b2)

# TODO: Check for greater and lesser value
print("Is b1 price greater than b2 :",b1>b2)
print("So its not lower? :",b1<b2)
# TODO: Now we can sort them too
print("-------------------\nBOOKS:")
Book.showbooks()
Book.books.sort()
print("-------------------\nSORTED:")
Book.showbooks()

