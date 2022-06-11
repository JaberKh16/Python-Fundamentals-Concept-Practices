"""
    Modules In Python Concept
    =========================
    a) What are Python Modules?
        --  In Python, Modules are simply files with the “.py” extension 
            containing Python code that can be imported inside another 
            Python Program.

            In simple terms, we can consider a module to be the same as a 
            code library or a file that contains a set of functions that 
            can be included in another program.
            
    b) What things usually Modules contains?
        -- Module contains the following components:

            i.  Definitions and implementation of classes,
            ii. Definitions of Variables, and Functions
        
    c) How to create Python Modules?
        --  To create a module, need to create a file containing the sub task of
            code and saving the file as extension ".py". Now, the name of the
            file becomes the name of the module.
            For Example-
                addition_module.py
                ------------------
                def addition_of_numbers(nums):
                    sum = 0
                    sum +=nums;
                    return sum;
                
                working_program.py
                ------------------
                import addition_module # to import the module file
                
                
    Advantages of Modules
    ---------------------
    Some of the advantages while working with modules in Python is as follows:

        a) Reusability
            --  Working with modules makes the code reusable.

        b) Simplicity
            --  The module focuses on a small proportion of the problem, 
                rather than focusing on the entire problem.

        c) Scoping
            --  A separate namespace is defined by a module that helps 
                to avoid collisions between identifiers.
                
    Python Built-in Modules
    ------------------------
    Python interaction shel provides many built-in functions to work with
    certain operations. Those functions are basically bundled up and gets
    loaded when Python shell is being started. Some of those functions are
    following-
    
        i.   print() and input() for I/O,
        ii.  Number conversion functions such as int(), float(), complex(),
        iii. Data type conversions such as list(), tuple(), set(), etc.

    In addition to these many built-in functions, there are also a large number 
    of pre-defined functions available as a part of libraries bundled with 
    Python distributions. 
    
    These functions are defined in modules which are known as built-in modules.

    These built-in modules are written in C language and then integrated with 
    the Python shell.
    For Example-
        # To list all the  available modules in Python use the function-
                
                    >>> help('modules') 


"""

import getting_greattings_module as gretting # getting the 'getting_greattings_module' module
import addition_numbers_module as addition_operation # getting the 'addition_numbers_module'

message = gretting.message_grettings()
print("Gretting message is: ", message)

summation_result = addition_operation.addition_of_numbers([1,2,4,6,10])
print("Summation result is: ", summation_result)

