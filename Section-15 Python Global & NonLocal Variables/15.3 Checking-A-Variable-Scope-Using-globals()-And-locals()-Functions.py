"""
    Checking Variable Scope Using globals() and locals() Functions
    ===============================================================
    Python has two built-in methods named- globals() and locals(). 
    They allow you to determine whether a variable is either part 
    of the global namespace or the local namespace.
    
    
"""
# defining the function
def places_name():
    # making this 'place' variable having the global namespace
    global place
    place = "Cape Town" # update the value of 'place'
    name = "John"
    
    print("'place' in global:", 'place' in globals())
    print("'place' in local :", 'place' in locals())
    print("'name' in global :", 'name' in globals())
    print("'name' in local  :", 'name' in locals())
    return

# defining a variable 'place' which has global space 
place = "Berlin"
print(place)

# calling the function
places_name()
