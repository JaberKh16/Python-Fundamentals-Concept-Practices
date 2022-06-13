'''
    [Iteraor Object Exception]
    ===========================
    Iterator Object raise an Exception named "StopIteration" in 2 cases
    which are the followin-
        
        1.  If an iterator has no value to be iterated or access upom. 
        2.  If an iterator all values is being accessed or iterated already 
            and has no more value to access, which means iterator is 
            being exhausted.
            
    So, When no more data are available "StopIteration" exception is being 
    raised instead. 
    
    At this point, the iterator object is exhausted and any further calls to 
    its __next__() method just raise "StopIteration" Exception again.
            
            
'''

# declaring a List
nums = [1, 2, 3, 4]

# making the list an iterator object using iter() method
i_nums = iter(nums) # iterator having 4 values 

try:
    # accessing the iterator using next() 
    print(next(i_nums)) # accessing the 1st value
    print(next(i_nums)) # accessing the 2nd value
    print(next(i_nums)) # accessing the 3rd value
    print(next(i_nums)) # accessing the 4th value
    
    # now trying to access the 5th value, although there has no 5th value of 
    # this oterator thus raise an exception "StopIteration"
    print(next(i_nums)) # because already all the values of iterator is being iterated or accessed

except Exception as e:
    raise e
