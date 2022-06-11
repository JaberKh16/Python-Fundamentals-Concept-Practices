'''
    More About Keyword Argument
    ===========================
    #   With keyword argument you can specify the keyword while passing 
    #   value to the keyword argument
    #   By convention, keyword argument use --> **kwargs  to specify 
        keyword argument but any name can be set as the keyword argument.
    
    #   Keyword Argument will return the dictionary data type.
'''

# defining the function
def department_names(**kwargs): # setting the keyword argument named as '**kwards'
    return kwargs

# calling the function
dept_id = department_names(CSE="011", EEE="021", Economics="031" , CIVIL="041")
print(f"Keyword Argument Data Type is: {type(dept_id)}")
print(dept_id)