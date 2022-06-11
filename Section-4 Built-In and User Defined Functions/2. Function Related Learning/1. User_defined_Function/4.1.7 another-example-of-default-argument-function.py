"""
    Default Argument Value Function
    ================================
    #   Default Argument Value is the argument value which is being set 
        to the function as an argument at the time of the function 
        declaration. 
    #   If no argument is being passed for the default valued argument from 
        outside then the default argument value will be passed that 
        setted argument value.

"""

# defining the function
def person_info(name = "someone", age="unknown"):
    print(f"Name is:", name ,"and", "Age is:",age)


# calling the function without passing any paramter
person_info() 

# calling the function via passing parameter
person_info("Jaber")
person_info("Jaber", 24)
person_info(None, 24) # setting 'None' to 'name' parameter