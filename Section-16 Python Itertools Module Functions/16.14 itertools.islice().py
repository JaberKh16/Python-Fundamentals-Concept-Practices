"""
    itertools.islice() Function
    ==============================
    itertools.islice() Function is very much like slices and takes
    an iterable, allows to cut a piece of an iterable from that
    iterable.  
    
    Syntax-
        itertools.islice(iterable, start, stop [, step])
        
    
"""

# importing the islice() function from the module
from itertools import islice

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle', 'Pentagon', 'Square']
sliced_items = islice(shapes, 1, 3)

for slice_iterable in sliced_items:
    print(slice_iterable)