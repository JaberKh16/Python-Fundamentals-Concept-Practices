"""
    itertools.takewhile() Function
    ===============================
    itertools.takewhile() Function is the opposite of itertools.dropwhile() 
    function. This takewhile() function makes an iterator and returns the
    elements from the iterable as long as the predicate is true.
    
    Syntax-
        itertools.takwhile(predicate, iterable)
        
    Argument 'times' is used to define how many times we want the
    specified object to be repeated.
            
"""

# importing the takewhile function from the module
from itertools import takewhile
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = takewhile(lambda x: x<=6, data)
for values in result:
    print(values, end=',')
    
print("\n\n")

# another example with range() iterable   
nums = list(takewhile(lambda x : x<=6, range(1, 8)))
# print(nums) # uncomemnt it resulted the same as above