"""
    itertools.compress() Function
    =============================
    itertools.compress() Function filters one iterable with another.   
    
    Syntax-
        itertools.compress(data, selectors)
        
    Compress the 'data' which is an iterable depending on the 'selectors'
    which is another iterable.
    
"""

# importing the combinations() function from the module
from itertools import compress

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle']
selections = [True, False, True]
compressed_values = compress(shapes, selections)

for values in compressed_values:
    print(values)