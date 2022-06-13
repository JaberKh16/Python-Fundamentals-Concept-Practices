"""
    itertools.chain() Function
    ==========================
    itertools.chain() Function is used to take a series of iterables
    and chain them to get a single long iterable.
    
    Syntax-
        itertools.chain(*iterable)
        
            
"""

# importing the chain() from the module
from itertools import chain

# defining iterables
colors = ['red', 'blue', 'white', 'black', 'green' ]
shapes = ['circle', 'rectangle', 'square', 'pentagon']

# combining above those iterables through chain() function
combined_chain = list(chain(colors, shapes))
print(combined_chain)