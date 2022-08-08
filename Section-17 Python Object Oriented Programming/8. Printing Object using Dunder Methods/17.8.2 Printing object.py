'''
  # Printing Object gives us information about object we are working with
  # In Python , this process can be achieved by using following methods--

    1. __repr__
     
        # Now, __repr__() function returns a string containing a printable 
        # representation of an object.
        # It could be any valid python expression such as tuple, dictionary, string etc. 
        # This method is called when repr() function is invoked on the object, 
        # in that case, __repr__() function must return a String otherwise 
        # error will be thrown.
        # __repr__ goal is to be unambiguous.
             
    2. __str__
                
        # __str__ goal is to be readable.Means use __str__ when need a textual representation.
        # __str__ returns a string containing a nicely printable representation of an object. 
        #  For strings, this returns the string itself. 
        # If you print an object, or pass it to format, str.format, or str,
        # then if a __str__ method is defined, that method will be called,
        # otherwise, __repr__ will be used.
        # The difference with repr(object) is that str(object) does not always attempt
        # to return a string that is acceptable to eval();its goal is to return a printable string. 
        # If no argument is given, returns the empty string.

  

'''

class Test :

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a : %s, b : %s" %(self.a, self.b)
    

    def __str__(self):
        return "From str method of Test : a is %s, b is %s" %(self.a, self.b)


t = Test(1234, 5678)
# this will print from __str__
print(t)

# this will print from __repr__
print([t])