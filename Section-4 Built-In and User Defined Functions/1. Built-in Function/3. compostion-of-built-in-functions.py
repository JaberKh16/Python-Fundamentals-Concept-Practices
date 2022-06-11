"""
    [Composition Of Functions Related Learning]

        #   Composition of function means chaining of functions.
        #   In other words, chaining of multiple built-in functions.
            
            For Example-
                
                math.sin(math.radians(value))
"""

# Importing Necessary Module
import math

# Calculating Radian Value From a Degree Value
degree = 30
print("Radian Value From Degree Value:", math.radians(degree))

# Incorrect Way Of Sine Value
print("Sine Value:", math.sin(degree)) # will results incorrect value

# Correct Way Of Sine Value - with compositon of functions
print("Sine Value:", math.sin(math.radians(degree))) # will results correct value