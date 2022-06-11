"""
    # Slicing Technique in Python
    ==============================
    # A part of any sequence/iterables is basically called slice.
    # Slicing can be applicable with string/list/tuple/array objects.
    # General Syntax for Slicing is the following:
        
        sequence[start: end: stepping] // Slicing General Structure
        
    # With Slicing Techniques generally [start: end: stepping] are designed as follows:
        
        1) start    --> if not defined default is 0
        2) end      --> if not defined default is last index which is -1
        3) stepping --> if not defined by default is 1
    
    # In Slices start included and end is excluded logically so it will be something
    # like this if you expressed mathematically :

            sequence[start, end)
                    
    # In Python, Slicing can be done in 2 ways:
        1. Postive Slicing 
        2. Negative Slicing

"""

# working with String Data Type
x = "Hello Python !!! U r Fucking Awsome"
print(x) # will print the whole string object 'x'

# slice the Data Type
# slicing is done with (:) operator via providing the index value to it

# note : In Slicing Technique -->  say , object[start:end]; values inluded "start" upto "end"(excluding or leaving end) 
# if nothing is specified as x[:end] then by default including from 0th index as "start" value upto specified "end" 
print(x[:-1]) # will print the string object 'x' value from 0th index upto -1th index(removed the last index)
print(x[:-8]) # will print the string object 'x' value from 0th index upto -8 index
print(x[1:3]) # will print string object 'x' value from 1th index upto 3th index
print(x[-3:-1]) # will print string object 'x' value from -3th index upto -1th index