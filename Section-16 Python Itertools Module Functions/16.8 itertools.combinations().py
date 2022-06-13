"""
    itertools.combinations() Function
    ==================================
    itertools.combinations() Function takes an iterable and an integer
    and then creates all the unique combinations that have 'r' members
    where 'r' is basically the integer value.    
    
    Syntax-
        itertools.combinations(iterable, r)
        
            
"""

# importing the combinations() function from the module
from itertools import combinations

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle']
resulted_combination = combinations(shapes, 2)

for values in resulted_combination:
    print(values)