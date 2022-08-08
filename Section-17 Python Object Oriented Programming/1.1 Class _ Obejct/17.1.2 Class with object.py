"""
    Python Class Object Concept
    ============================
    #   Object - An object is an instance of a class.When a class is defined
        only the description for the object is defined. And this process
        creating a object is called instantiation

    #   Methods-  Methods are the functions defined inside the class block.
        They are used to define the behaviours of the class.

    Note-   When a object is created if you won't pass the 'self' as an argument of
            methods then it gives an TypeError : saying 1 arguments is given
            this is because whenever a object call it's methods, the object
            basically passed itself as an argument to the method.

            scenario : Obj1.func()  translated into Object_name.func(obj1)
            
"""

# defining the class
class Parrot :

    # class attributes 
    name = "Parrotie"
    color = "Green"
    
    # instance methods
    def fly(self):
        print("I can fly")

    def swim(self):
        print("I can't swim")

# creating a class instance        
bird = Parrot()

print('Class Information')
print('====================================================================')
# checking class name
print(f'Class Name and Info : {bird}')
print('====================================================================')

print('Instance Attributes Info')
print('====================================================================')
# class instance attributes
print(f'Bird Name: {bird.name}')
print(f'Bird Color: {bird.color}')

print('====================================================================')
print('Instance Methods')
print('====================================================================')
# class instance methods
bird.fly()
bird.swim()

# via class name calling instance methods
print('====================================================================')
print('Instance Methods Location')
print('====================================================================')

print(Parrot.fly)
print(bird.fly)



