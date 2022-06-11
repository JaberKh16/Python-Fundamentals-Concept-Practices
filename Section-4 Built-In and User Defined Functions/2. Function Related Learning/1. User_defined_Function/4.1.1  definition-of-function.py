"""
    [Non-Parameter Function Declaration]
"""

# defining the function
def my_function():
    print("this is a function call in Python")
    print("I m awsome")


# now this follow calling the user defined function calling itself
my_function()
# it returns 'None' after function block returns it block statement
# because it itself taken as print (function_name()) returns 'None'
# after function work has been done, it print(func_name) doesn't 
# returns any value e.g None
print(my_function())