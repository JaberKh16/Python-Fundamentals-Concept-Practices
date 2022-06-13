'''
    Definition of Iterator
    ========================
    An object with a state(having memory),so that it remembers where it
    is during the iterations.
    
    Iterator is an iterable that remembers its state. Which means, it's 
    a Python object with a state so it remembers where it is during 
    iteration.
                    
    Iterators is nothing but a Python Object which return one data
    at a time during its iteration over the stream of data.
    
    
    To Create a Iterator Object
    ============================
    We can make Python Mutuable Datatype into a Iterator Object
    in 2 ways,
        1. iter() function --> to create an Iterator Object
        2. __iter__() method --> to create an Iterator Object
    
    Note to Rememeber-
    1.  iter() function needs to pass the object we wanted to be an Iterator Object.
        For Example-     
                    iter(object) 
    
    2.  __iter__() method nedes to be called by the object to become an Iterator Object 
        of that Object.
        For Example- 
                    object.__next__()

    Here's the "object" is the Iterables such as lists , tuples, sets, strings and many more
    Python objects.
    
'''


# defining a List
nums = [1, 2, 3, 4]

# making the list an Iterator Object using __iter__() function
i_nums = nums.__iter__()


# this will show the object type for the variable
print(type(i_nums)) # will returns object type  <class 'list_iterator'>, so this is a list-type iterator object

# Declaring another list object
number = [2, 4, 5, 6, 7,8]

# making the list object an Iterator Object using iter() method
i_numb = iter(number)

# checking the methods that the Iterator Object have
# this will show all the dunder methods for the iterators
print(dir(i_nums))

