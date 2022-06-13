''' 
    Accessing Technique for Iterators
    ==================================
    To get access the Iterator or to get the values of Iterator 
    we can use the dunder method( __next__() )function or 
    next() method. 
    
    Rememeber, 
        1.  With the next() function, need to pass the iterator object. 
            For Example-
                    next(object) 
        2.  With the __next__() method nedes to be called by iteraor object. 
            For Example-
                    object.__next__()
    
    Although both are equvalent and doing the same work.
'''

# declaring a list
nums = [1, 2, 3, 4]

# making the List an iterator object using __iter__() function
i_nums = nums.__iter__() # can be done via iter() method also

# accessing the iterator can be done, either using next() or __next__()
print(next(i_nums)) # acessing using next() method
print(next(i_nums)) # accessing using next() method
print(i_nums.__next__()) # accessing using __next__() function
print(i_nums.__next__()) # accessing using __next__() function
