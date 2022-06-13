"""
    Non Local Variable Concept
    ==========================
    Python3 introduced Non-local Variables as a new kind of variables.
    To make a variable a Non-local Variable needs to define it using
    the keyword 'nonlocal' with the variable name.
    
    Non-local Variables have a lot in common with Global Variables. 
    One difference to Global Variables lies in the fact that it is not 
    possible to change variables from the module scope-
    
    i.e. variables which are not already defined inside of a function, 
    by using the 'nonlocal' statement and hits an SyntaxError exception
    saying the following-
            
            SyntaxError: no binding for nonlocal 'var_name' found
        
    Thus Nonlocal bindings can only be used inside of nested functions.
    A Non-local Variable has to be defined in the enclosing function scope. 
    Also, that Non-Local Variable has to be defined with a value inside its 
    outer function scope. 
    
    If the variable is not defined in the enclosing function scope, 
    the variable cannot be defined in the nested scope. 
    This is another difference to the "global" semantics.
    
    Also, assignemnt operations to the Non-local Variables is not
    posssible and hits an SyntaxError exception if its not defined
    inside a nested function.
    
"""

# defining the function
def non_local_var_example():
    nonlocal message 
    print(message)

# defining a variable
message = 'Songs to listen'
# calling the function
non_local_var_example()
