"""
    [Python Mathematical Related Built-in Functions]

    #   In Python, some built-in functions are those are there to perform  
        mathematical related operations.
    #   Those functions are the following:

            1)  sin()          --> to perform trigonometric sine operation
            2)  cos()          --> to perform trigonometric cosine operation
            3)  tan()          --> to perform trigonometric tangent operation
            4)  tanh()         --> to perform trigonometric hyperbolic tangent operation
            5)  radians()      --> to perform trigonometric radians operation
            6)  sqrt()         --> to perform mathematical square root operation
            7)  factorial()    --> to perform mathematical factorial operation
            8)  exp()          --> to perform mathematical exponential operation
            9)  floot()        --> to perform mathematical floor operation
            10) ceil()         --> to perform mathematical ceil operation
            
            and many more ....................................................
            ..................................................................
            ..................................................................
"""
# Importing the 'math' module
import math

# Calculating Perimeter Of a circle
radius = 4
print("Circle Perimeter:", (2 * math.pi * radius))

# Calculating Radian Value From a Degree Value
degree = 30
print("Radian Value From Degree Value:", math.radians(degree))

# Calculating Ceil Of a Number
ceil_value = math.ceil(34.6)
print("Ceil Value Of a Number:", ceil_value) 

# Calculating Floor Of a Number
floor_value = math.floor(34.8)
print("Floor Value Of a Number:", floor_value)

# Calculating The Square Root Of a Number
sqrt_value = math.sqrt(16)
print("Square Root Value Of a Number:", sqrt_value)

# Calculating The Exponential Of a Number
exp_value = math.exp(16)
print("Exponential Value Of a Number:", exp_value)


# Calculating The Factorial Of a Number
factorial_value = math.factorial(5)
print("Factorial Value Of a Number:", factorial_value)