"""
    itertools.permutations() Function
    ==================================
    itertools.permutations() Function takes an iterable and then performed
    its permutations.  
    
    Syntax-
        itertools.permutations(iterable, r=None)
        
    
"""

# importing the permutations() function from the module
from itertools import permutations

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle', 'Pentagon', 'Square']
permutations_result = permutations(shapes)

for permutations_values in permutations_result:
    print(permutations_values)