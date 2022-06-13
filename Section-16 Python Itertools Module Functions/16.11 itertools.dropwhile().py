"""
    itertools.dropwhile() Function
    ==============================
    itertools.dropwhile() Function makes an iterator that drops elements
    from the iterable as long as the predicate is true and then afterwards
    returns every element.  
    
    Syntax-
        itertools.dropwhile(predicate, iterable)
        
    Here, 'predicate' could be any condition depending on which the
    dropping of elements would be done from the specified 'iterable'.
    
"""

# importing the dropwhile() function from the module
from itertools import dropwhile

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle', 'Pentagon', 'Square']
dropped_items = dropwhile(lambda item: len(item) < 8, shapes)

for item in dropped_items:
    print(item)