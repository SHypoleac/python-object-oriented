# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


# TODO: "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass():
    val1 : str = "Value 1"
    val2 : int = 0


obj = ImmutableClass(val1='kunkbungu')  # You can set the values of frozen class only with initialization
print(f"value 1 is {obj.val1}, and 2 is {obj.val2}")

# TODO: attempting to change the value of an immutable class throws an exception


# TODO: even functions within the class can't change anything
