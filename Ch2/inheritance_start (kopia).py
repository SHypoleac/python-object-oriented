# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance

#TODO: Create a class "Publication" with attributes "title" and "price"
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

#TODO: Create a class "Perdiodicaly" that inherits from "Publication"
# and additionally has attributes "period" and "publisher"
class Perdiodicaly(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

#TODO: Allow the "Book" class to inherit attributes from Publication
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

#TODO: The Magazine and Newspaper classes can inherit all atributes from "Perdiodicaly"
class Magazine(Perdiodicaly):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Perdiodicaly):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")
