"""
    itertools.repeat() Function
    ============================
    itertools.repeat() Function is used to repeat an object over and 
    over again, unless there is a 'times' argument specified.
    
    Syntax-
        itertools.repeat(object [, times])
        
    Argument 'times' is used to define how many times we want the
    specified object to be repeated.
            
"""

# importing the necessary function
from itertools import repeat

for i in repeat("Apple", 4):
    print(i)
