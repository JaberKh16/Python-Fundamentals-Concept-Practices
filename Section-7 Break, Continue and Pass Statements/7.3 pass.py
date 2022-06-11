'''
    pass Statement
    --------------
    pass Statement is a keyword in Python which is used for those statements
    which we want to define later but for now skipping the definition.
    
    # Lets, understands with a programm

        
        # using with loop 
        >>>   for x in range(1, 10):
                    pass   # it returns 9(terminated_value)
                print(n)
    1.  'it' passes the to end and returns its end(stop) value
        means it also a skipper in looping which controls the
        loop executing as given and the last executing value
        where it's get terminated- 
            e.g returns with terminated_value
            
        # using with function
        
        >>> def function_name():
                pass
'''

# working with 'pass'
# it passes the loop to its end and as a value returns the terminated_value
n = 0
for n in range(1, 10):
    pass
print(n)

# working with function
def not_defined():
    pass