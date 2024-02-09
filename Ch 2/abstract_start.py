# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

#TODO: Import "ABC"(abstract base classes) and abstractmethod from abc
from abc import ABC,abstractmethod

#TODO: Inheriting from ABC indicates that this is an abstract base class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
        self.area=0
    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calcArea(self):
        return self.area

#TODO: Create specific versions of "calcArea" for different shapes
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        self.area=(3.14*self.radius**2)
        return self.area

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        self.area=(self.side*self.side)
        return self.area

# Abstract classes can't be instantiated themselves
# g = GraphicShape() # this will error
        
#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
