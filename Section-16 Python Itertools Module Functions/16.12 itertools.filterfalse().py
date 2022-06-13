"""
    itertools.filterfalse() Function
    =================================
    itertools.filterfalse() Function makes an iterator that filters elements
    from the iterable returning only those for which the predicate is False.  
    
    Syntax-
        itertools.filterfalse(predicate, iterable)
        
    Here, 'predicate' could be any condition depending on which the
    filtering of elements would be done from the specified 'iterable'
    only for which the 'predicate' condition is False and those filtered
    elements will be returned.
    
"""

# importing the filterfalse() function from the module
from itertools import filterfalse

# defining iterables
shapes = ['Circle', 'Rectangle', 'Triangle', 'Pentagon', 'Square']
filtered_items = filterfalse(lambda item: len(item) < 8, shapes)

for filtered_item in filtered_items:
    print(filtered_item)