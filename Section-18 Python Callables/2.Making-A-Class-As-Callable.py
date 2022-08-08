'''
    Making A Class As Callable
    ==========================
    Functions and classes are both callables and can actually create 
    own callable objects too.

    For Example-
    >>> class Person:
            def __init__(self, name):
                self.name = name
            def __call__(self): # defining a __call__ method to make it callable
                print("My name is", self.name)
    
    
    Classes are callable and we call the Person class to get back 
    to get back an instance of that class:
    >>> person1 = Person("Jack")
    >>> print(person1) # returns <__main__.Person object at 0x7fbf9f3331c0>
    
    But the Person object is also callable! We can call that Person object 
    by putting parentheses after it:
    >>> person1() # returns 'My name is Jack'
    
    This works because we've implemented a __call__ method on the Person class. 
    Adding a __call__ method to a class makes its class instances callable.

    In fact, anything with a __call__ is a callable and all callables have 
    a __call__ method. Even functions and classes have a 
    __call__ method (that's how they're callable):
    
    >>> print(enumerate.__call__) # returns <method-wrapper '__call__' of type object at 0x56322b9cb580>
    >>> print(function_name.__call__) # returns <method-wrapper '__call__' of function object at 0x7fbd631cd940>

'''

# defining a callable class
class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    # defining __call__ to make the class as callable
    def __call__(self):
        print(f"Person name is: {self.name}")

person1 = Person('Jack')
print(person1) # returns the class object
print(person1()) # calling the class object 