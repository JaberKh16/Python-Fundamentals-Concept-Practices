"""
 Abstract Class:
 
  # Abstract is the base class for any user defined or derived classes, 
    means Abstract class can only be inheritant by other derived class.
  # Abstract class doesn't have any instance of its own, if you try to
    create a instance of abstract class it will through a TypeError.

  # Abstract class shouldn't have the definition of the derived class 
    overidden methods , it only just have the overidden method declaration.
    and this declared method should be declared with '@abstractmethod' decorator
    which let this method tell the class that its the abstract method for this
    base class and will be defined in the derived classes.


"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    name = 'Square'
    side = 4
    def area(self):
        print(f'Area of {self.name} is : {self.side * self.side}')
        

class Rectangle(Shape):
    name = 'Rectangle'
    widht = 5
    length = 10
    def area(self):
        print(f'Area {self.name} is : {self.widht * self.length}')

class Circle(Shape) :
    name = 'Circle'
    pi = 3.1416
    radius = 4
    def area(self):
        print(f'Area of {self.name} is : {self.pi * (self.radius * self.radius)}')



try :
    # creating the derived class instances
    circle = Circle()
    rectangle = Rectangle()
    square = Square()
    

    # calling class instace method area() 
    circle.area()
    square.area()
    rectangle.area()

except Exception as e:
    print(e)
