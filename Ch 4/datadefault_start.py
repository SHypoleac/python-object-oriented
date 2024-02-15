# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

# TODO: Import "field" function from dataclasses
from dataclasses import dataclass, field

# TODO: Define a function that returns a random number between 20-40.
# Don't forget to import the necessary module
import random
def losowa_liczba():
    return random.randint(20,40)

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    # TODO: Use the field function to get default price as random number
    price: float = field(default_factory=losowa_liczba)

b1=Book()
b2=Book()

print (b1,"\n",b2)
