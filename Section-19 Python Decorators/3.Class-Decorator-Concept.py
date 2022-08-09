'''
    Decorator Class Basic Concept
    ============================
    A decorator can also be a function which accepts a class 
    (a "decorator function" that can be used as a "class decorator").
    
    Now which mean decorating a class is possible. To decorate the class
    see the following example-
    >>> @dataclass
        class ClassName:
            var: float

        @property
        def area(self):
            return self.var**2 
    
    The @dataclass is a class decorator made which is used to make the class
    initializer for us, Meaning that we don't need to use __init__ inside a class
    to make the initialization, @dataclass decorator does it foe us.
    
    It also made a __repr__ method, so our Class objects have a nice 
    string representation.
    
    To use the 'dataclass' decorator need to import it from the 
    "dataclasses" module.
    
'''

# importing the 'dataclass' decorator from dataclasses module
from dataclasses import dataclass

# making the class decorator
@dataclass 
class Square:
    width: float # defining a instance which takes float type 
    # defining the decorator
    @property # property decorator accepted a function and will return property object
    def find_area(self):
        return self.width ** 2
    
print(Square) # returns a class object
print(Square.find_area) # return a class property decorator object
print(Square(2))

# creating a class instance and see
square = Square(20.50)
print(square)

