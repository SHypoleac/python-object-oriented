# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

#TODO: For A and B class create an attribute "name" that will take different values
class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name="Strawberry"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name="Banana"


class Fruits(B,A):
    def __init__(self):
        super().__init__()
    #TODO: Create a class method "showprops" returning the attributes it owns
    def showprops(self):
        return self.prop1, self.prop2, self.name


#TODO: create the object of the class "C" and call showprops()
c = Fruits()
print (c.showprops())
#TODO: You can also call "Class.__mro__" to find out all the parent classes
print (Fruits.__mro__)