"""
    Global Variable Access Using "global" Keyword
    ==============================================
    The value of a global variable can be accessed throughout the entire 
    program. In order to achieve that from within functions, 
    Python offers the usage of the keyword 'global'.
    
"""

# declaring a Normal Variable without declaring it as global
x = "global existence" # this variable 'x' has Global Scope thus it's Global Variable
print("\nMaking a Normal Variable Scope to Global Variable Scope using \"global\" Keyword\n")

def some_function():
    # declaring a Global Variable
    # this variable 'x' has now global scope because of "global" keyword
    # or can say this variable 'x' is now refering the same above variable 'x' because of it's beign global now
    global x ; 
    x = "Change of Global x value" # changing the global variable 'x' value
    # declaring a function Local Variable
    y = " 'y' is local to this function" # this variable 'y' has local scope
    print(f"Local Scope y = {y}") # will print the local variable 'y' value
    print(f"Global Scope x = {x}") # will print the global variable 'x' value 


# before calling the function check variables 'x' value which has global namespace
print(f"Variabe x = {x}") # will print the variable 'x' value having the global namespace

# calling the "some_function()" to see variable existance
some_function()
print(f"Global x = {x}") # will print the global scope variable 'x' changed value


