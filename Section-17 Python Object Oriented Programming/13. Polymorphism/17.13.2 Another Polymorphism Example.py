
class Rectangle:
    name = 'Rectangle'
    def __init__(self, length, breadth) -> None:
        self.length  = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    

class Triangle:
    name = 'Triangle'
    def __init__(self, s1, s2, s3) -> None:
        self.s1  = s1
        self.s2  = s2
        self.s3  = s3
    
    def area(self):
        sp = (self.s1 + self.s2 + self.s3)/2
        return ( sp * (sp -self.s1) * (sp - self.s2) * (sp - self.s3) )
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
class Circle:
    name = 'Circle'
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return 3.1416 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.1416 * self.radius
    



while True :
    # creating instance of classes
    r1 = Rectangle(13, 25)
    r2 = Rectangle(14, 16)
    t1 = Triangle(14, 17, 12)
    t2 = Triangle(25, 33, 32)
    c1 = Circle(14)
    c2 = Circle(25)

    # creating a polymorphic function
    def find_area_perimeter(shape):
        print(f'Geometric Object is : {shape.name}')
        print(f'Area is : {shape.area()}')
        print(f'Perimeter is : {shape.perimeter()}')

    choice_of_instance  = int(input('Enter the instance choice :'))
    if choice_of_instance == 1:
        find_area_perimeter(t2)
    elif choice_of_instance == 2:
        find_area_perimeter(r1)
    elif choice_of_instance == 3:
        find_area_perimeter(c2)
    elif choice_of_instance == 0:
        print('Exiting....')
        exit()