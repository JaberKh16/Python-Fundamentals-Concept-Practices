"""
    Variable Scope Related Exception Concept
    ========================================
    If inside the use defined function any variable which is being 
    declard outside the function(thus having the global namespace) 
    been printed or called then it will hits an exception saying
    the following-
    
    UnboundLocalError: local variable 'var_name' referenced before assignment
    
    In the above exception occurs because any variable declared upon the function
    is considered as having the local namespaces.
"""

# defining the function
def message_printing(): 
    print(message)
    message = "I love London!"
    print(message)

# defining the variable
message = "I love Paris!"

try:
    # calling the function
    message_printing()
except UnboundLocalError as error:
    print(error)
