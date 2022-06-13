"""
    itertools.combinations_with_replacement() Function
    ==================================================
    itertools.combinations_with_replacement() Function takes an iterable and 
    an integer and then creates a combinations that have 'r' members 
    which here denotes the individual elements to be repeatted 
    more than once.   
    
    Syntax-
        itertools.combinations_with_replacement(iterable, r)
        
            
"""

# importing the combinations_with_replacement() function from the module
from itertools import combinations_with_replacement

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle']
resulted_combination = combinations_with_replacement(shapes, 2)

for values in resulted_combination:
    print(values)