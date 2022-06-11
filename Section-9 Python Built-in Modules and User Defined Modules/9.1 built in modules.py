'''
        Working With Built-in And Any Modules
        ======================================
        
        Syntax : 1.import module_name(direct import module)
                2. from module_name import module_name(some function from module)
                3. importing can be done in 2 ways---->
                        a) by module_name --> when directly want to import the module 

                                e.g- import module_name


                        b) by function_name --> when want to importn specific function from the module

                                e.g- from module_name import function_name

        # To access the module we need to use,
                v = module_name.inside_function()
        Here, inside_function is the inside function importing module have

'''


# directly importing module 'math'
import math

# using the module funciton math.factorial()
factorial_value = math.factorial(5)
print("Factorial is :",factorial_value)

# from module 'math' importing specific function 
from math import factorial

print("Factorial of 6 is : " ,factorial(6))

from math import pi
print("Pi Value is : ", pi)


# from math import sqrt
import  math
sqrt_value = math.sqrt(9)
print("Squre Root of 9 is : " , sqrt_value)

# Aliases the module name 
# syntax : import module_name as alias_name

import math as m # it treats the 'math' module as 'm' for that module
print("Sqaure Root of 9 is : " , m.sqrt(9))




