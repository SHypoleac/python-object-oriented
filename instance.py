# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, pages, price):
        self.title = title
        # TODO: add properties
        self.pages = pages
        self.price = price
        self.__secret=1
    # TODO: create instance methods
    def showprice(self):
        "Show must go on"
        if hasattr(self,"_ulululu"):
            self.price-=(self.price*(self._ulululu/100)*self.__secret)

            x="after discount",self._ulululu,"% is",self.price
        else:
            x="without discount is",self.price
        print ("The price of",self,x)
    def setdiscount(self,amount):
        self._ulululu=amount

# TODO: create some book instances
b1 = Book("War and Peace",1336,30)
b2 = Book("The Catcher in the Rye",224,9.99)

# TODO: print the price of book1
b1.showprice()

# TODO: try setting the discount
b1.setdiscount(10)
b1.showprice()

# TODO: properties with double underscores are hidden by the interpreter
