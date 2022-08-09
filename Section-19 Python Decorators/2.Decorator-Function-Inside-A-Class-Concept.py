'''
    Decorator Functions Or Decorator Class
    ======================================
    A decorator can be a class which accepts a function and returns an instance  
    of that class (a "decorator class" that can be used as a "function decorator").

    A decorator can also be a function which accepts a class 
    (a "decorator function" that can be used as a "class decorator").
    
    For Example-
    >>> class ClassName:
            def __init__(self, var):
                self.var = var
            @property
            def function_name(self):
                return var
                
    That 'property' decorator accepted a function but it didn't return a 
    function, it returned a property object instead-
        >>> ClassName.function_name # <property object at 0x000001CED0DC1360>
        
    The property decorator that's built-in to Python is actually a class.
        >>> property # <class 'property'>
        
    The built-in property decorator is a class which accepts a function 
    (the function_name() method in above case) and returns an instance 
    of the property class.

    So,Function decorator (a decorator used for decorating functions) isn't a 
    decorator function so much as a decorator class (meaning it's implemented 
    using a class under the hood). But the thing we care about is that it's 
    a callable that accepts a function, so we can use it the same way as 
    any other decorator.
    
    A decorator is a callable (usually a function though sometimes a class) 
    that accepts either a function or a class and returns a new function 
    or class that wraps around the original one.

'''

class Square:
    def __init__(self, width) -> None:
        self.width = width
    # defining the decorator
    @property # property decorator accepted a function and will return property object
    def find_area(self):
        return self.width ** 2
    
print(Square) # returns a class object
print(Square.find_area) # return a class property decorator object