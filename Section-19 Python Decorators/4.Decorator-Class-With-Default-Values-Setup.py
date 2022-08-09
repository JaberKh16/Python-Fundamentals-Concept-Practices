'''
    Decorator Class With Default Values
    ===================================
    It is very easy to set decorator with default values. "dataclass"
    module makes it very handy.
    Syntax-
        @dataclas
        class ClassName:
            var1: str
            val2: int = 45
            val3: float = 53.3
            
    # to access those value use-
        class_instace.val1
        
'''
# importing the 'dataclass' decorator from dataclasses module
from dataclasses import dataclass

# making the class decorator
@dataclass
class Person:
    name: str
    gender: str
    height: float = 5.6
    salary: int = 20000


# creating a class instance
person1 = Person('Jack', 'Male')
print(person1)
# accessing only the name
print(person1.name) 
print(person1.__dataclass_fields__)