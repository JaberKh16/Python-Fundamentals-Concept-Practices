"""
    Python Class Concept
    ====================
    # Python supports OOP Features , here OOP means Object Oriented Programming
    # Definition-  solving a problem with creating a object
    # An object has two characteristic -
            1. Attribute or other_name e.g var
            2. Behaviour or other_name e.g methods

    # This OOP features come to provide reuseability of code.
    # Table of Contents for OOP -
        
        1. Class & Object
        
        2. Inheritance
        
        3. Encapsulation / Data Hiding
        
        4. Polymorphism
        
        5. Method Overidding
        
        6. Method Overloading
        
        7. Operator Overloading
        
    # Class - A class is blueprint for an object. 
    # Syntax -  class Object_name :
                    statement1
                    statement2
                        
    #   In Python, a class has it objects class already define, which provides 
        the facility to access all class members and to check this Python has 
        mro() method which gives a list of class object. 

"""


# define an empty class
class Empty :
    pass

# a class without object creation
class Car :

    "This is class programme with simple car definition"

    # class attributes
    name = "Ford GT"
    model = "173GT-R"
    color = "Dark Brownish"

    # class methods
    def engine_start():
        print("BHHHHHHHHHHHHHH")

    def change_gear():
        print("I have Gears")

    def turn():
        print("I can turn left or right")
        

print('Class Information')
print('====================================================================')

# checking class name 
print(f'Class Name and Info :{Car}')
# class instance attributes or variables


print('Instance Attributes Info')
print('====================================================================')
print(f'Car Name :{Car.name}')
print(f'Car Model Name :{Car.model}')
print(f'Car Color :{Car.color}')

print('Instance Methods')
print('====================================================================')

# class instance methods
print(Car.engine_start) # this will return the instance method location
print(Car.engine_start())
print(Car.change_gear) # this will return the instance method location
print(Car.change_gear())


print('Class Other Information Dunder Methods')
print('====================================================================')

# this will returns a method resolutin order for class
# here , its the class name  and its parent class in list format
print(f'Class Hierarchy: {Car.mro()}')
# checking the specified docstring inside the class using dunder __doc__
print(f'Class Docstring: {Car.__doc__}')

# this will contains the class namespace means the class class instances info
# the class object values
print(f' Class Information or Namespace: {Car.__dict__}')

# __module__ returns the module name in which the class is defined
print(f'Class Module Name: {Car.__module__}')

# __name__ will returns the class name
print(f'Class Name: {Car.__name__}')

# __bases__ returns the base class of the defined class
print(f'Class Base: {Car.__bases__}')

# this will return class 'type'
print(f'Class Type: {Car.__class__}')


print()
print('Object Class Information Based Dunder Methods')
print('====================================================================')

# this will return the Basic Class Info
print(f'Object Class Info : {object}')

# this will return the object class 'type'
print(f'Object Class Type: {object.__class__}')

# this will returns the object class docstring
print(f'Object Class Docstring: {object.__doc__}')

# this will returns a method resolutin order for object only
print(f'Object Class Hierarchy: {object.mro()}')











