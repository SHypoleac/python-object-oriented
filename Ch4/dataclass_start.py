# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

#TODO: Import dataclasses from dataclass and apply decorator
from dataclasses import dataclass

@dataclass
class Book:
    title :str
    author:str
    pages:int
    price:float

# create some instances
b1 = Book("Mistrz i Małgorzata", "Michał Bułhakov", 399, 39.95)
b2 = Book("Wojna i Pokój", "JD Salinger", 234, 29.95)
b3 = Book("Mistrz i Małgorzata", "Michał Bułhakov", 399, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print (b1)

# TODO: comparing two dataclasses - they implement __eq__
print (b1==b3)
print(b1==b2)

# TODO: change some fields

## yes, it works!
