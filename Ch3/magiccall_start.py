# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    our_stock=100
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        print(f"You create Book object {self.title} and your stock is {Book.our_stock}")

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self):
        if Book.our_stock-self.price>0:
            Book.our_stock-=self.price
            print(f"You just bought {self.title} for {self.price} and your stock is now {Book.our_stock}")
        else:
            print(f"You have only {Book.our_stock} and you cant afford {self.price}")


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
b1()
b2()
b2()
b1()
