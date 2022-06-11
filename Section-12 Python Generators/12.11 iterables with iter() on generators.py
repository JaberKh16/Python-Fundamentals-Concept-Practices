"""
    Iterables With iter() Method
    ============================
    The Python iter() function returns an iterator for the given object.

    iter() function creates an object which can be iterated one element 
    at a time.
    
    iter() Function Parameters
    ---------------------------
    The iter() function takes two parameters:

        a) object - object whose iterator has to be created (can be sets, 
                    tuples, etc.).
        b) sentinel (optional) - special value that is used to represent 
                                the end of a sequence.
    
    Return Value From iter() Function
    ----------------------------------
    a)  The iter() function returns an iterator object for the given object.
    b)  If the user-defined object doesn't implement,
            __iter__(), and __next__() or __getitem()__, 
        
        the TypeError exception is raised.
    c)  If the sentinel parameter is also provided, iter() returns an 
        iterator until the sentinel character isn't found.
        
        
"""

def generator_on_string():
    my_string = "Python is fun"
    x = iter(my_string) # making the string as an iterator
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

print(generator_on_string())