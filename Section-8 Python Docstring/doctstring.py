"""
    DocString In Python
    ====================
    In Python Docstring is used to document something either a function,
    a class or anything.

    Docstring can be constructed using triple quotes in two following ways-
    
        a) using """ """ when multi-line docstring
        b) using ''' ''' when single-line docstring
    
""" 

def shout_message(word):
    """
    The value of the word parameter will be pass from them function
    call when directing passing string formatted value. 
    
    Args:
        word (string): the word value

    Returns:
        no value
    """
    print(word + "!")

shout_message("SHHSHHHHSHH") # passing a word to print
print(shout_message.__doc__) # __doc__ magic method is used see the DocString