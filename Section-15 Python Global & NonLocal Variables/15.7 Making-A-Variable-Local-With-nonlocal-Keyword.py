"""
    ["nonlocal" Keyword is used in Nested Function to ensure a Variable 
    Locality(Local Scope) is being preserved over the Nested Functon]
"""


# declaring a Nested Function
def outer_function():
    
    x = "message" # Local Variable 'x' local to its defined function
    def inner_func():
        # with "nonlocal" keyword ensuring we want the same variable 
        # 'x' value is being preserved here
        nonlocal x  # refering the same 'x' declared above 
        x = "sender-info" # updating the 'x' value
        print(f"Inner x = {x}") # prints the Non Local 'x' value
    
    # calling the inner_func()
    inner_func() # will print the inner_function() nonlocal 'x' value which is 'sender-info'
    print(f"Outer x = {x}") # will print the outer_function() local variable 'x' value 
                            # which is 'sender-info' thus being updated


# calling the outer_func() Function  
outer_function()

