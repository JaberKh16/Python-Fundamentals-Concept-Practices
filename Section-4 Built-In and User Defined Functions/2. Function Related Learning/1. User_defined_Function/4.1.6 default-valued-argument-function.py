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
def sum_value(x, y=10): # 'y' is the setted which is default value parameter
    print("Sum is :", x+y)

# passing single argument
sum_value(10)

# changing the default argument value via passing new value
sum_value(10, 15)