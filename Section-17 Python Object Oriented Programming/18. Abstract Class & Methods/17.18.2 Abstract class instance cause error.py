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
    # creating the base class instance , now this will through an error, 
    # because this class has the @abstractmethod declared , and the other
    # derived used this @abstract method
    shape = Shape()

    # calling class instace method area() 
    circle.area()
    square.area()

except Exception as e:
    print(e)