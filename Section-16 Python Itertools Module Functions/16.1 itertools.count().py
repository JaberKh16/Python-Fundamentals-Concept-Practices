"""
    itertools Module Concept
    ========================
    itertools Module is a collection of tools intended to be fast
    and use memory efficiently when handling iterators(like- list or 
    dictionary). 
    
    itertools is one of Python built-in module which standardizes a core
    set of fast, memory efficient tools that are useful by themselves
    or in combination. Together, they form an "iterator algebra" making
    it possible to construct specialized tools succinctly and efficiently.
    
    Some of the itertools tools are the following-
    1) count --> makes an iterator that returns evenly spaced values 
                starting with parameter 'start'.
                Syntax- itertools.count(start=0, step=1)

"""

# importing the 'count' tool from the itertools
from itertools import count


for i in count(3, 2):
    print(i)
    if i>=20:
        break

print("\n")
