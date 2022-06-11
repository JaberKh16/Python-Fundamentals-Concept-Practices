'''
    Keyword Arguement Concept
    =========================
    #   In Python, Keyword Argument is the argument which work on the basis 
        of keyword passing and it doesn't care about the parameter 
        order(basically used to resolve the Positional Argument problem
        because with positional argument if argument being passed as wrong
        order its specified in the function declaration then exception occurs).
    #   Keyword argument can resolve which value to go where when being 
        passed value via function.
    #   Keywords Arguments basically are the optional arguments.
    #   Many Python, default functions already have some optional 
        keyword arguments.
        For Example-
            print('', end='') # here, 'end' is the keyword argument

    # But, if we want we can also provide our own function with keyword arguments.

'''

# declaring the function
def person_info(name="someone", age="unknown"): 
    print(f'Name is:{name} and Age is:{age}')

# calling the function in unordered parameter fashion
person_info(age = 25, name="JK")

# calling the 'age' parameter, via keyword argument fashion 
person_info(age =24) 