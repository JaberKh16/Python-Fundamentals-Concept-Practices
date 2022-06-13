"""
    [A Program to understand Python Variable Scope]
"""

# declaring a variable without declaring it as global
x = "global existence" # this variable has Global Scope thus it's Global Variable
print("\nNow to check this variable global scope declaring a function and look it's existence\n")

def some_function():
    # declaring another variable having the same as the global one
    x = "local to this function" # this variable 'x' has local scope though it's been declared inside this function
    print(f"Local Scope x = {x}") # will print the local scope variable 'x' value

# calling the some_function() to see Variable Existance
some_function()
print(f"Global Variable x = {x}") # will print the global variable 'x'

