# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOKTYPES=("POEM","COMEDY","DRAMA")

    # TODO: double-underscore properties are hidden from other classes
    __thebooks=[]

    # TODO: create a class method
    @classmethod
    def get_booktypes(cls):
        print (Book.BOOKTYPES)

    # TODO: create a static method
    def getbooklist():
        return Book.__thebooks

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def __init__(self, title, booktype,coment=0):
        self.title = title
        Book.__thebooks.append(title)
        try:
            if booktype in Book.BOOKTYPES:
                self.booktype=booktype
                x=("Succesfully created a book with title : ",title)
            else:
                x=ValueError(title,"hasnt valid book type")
        finally:
            if coment==1:
                print(x)


# TODO: access the class attribute
Book.get_booktypes()

# TODO: Create some book instances
b1=Book("Mistrz i Małgorzata","DRAMA")
b2=Book("Podróże naukowe","SCIENCE")
b3=Book("Czynem i Słowem","POEM")

# TODO: Use the static method to access a singleton object
print(Book.getbooklist())
