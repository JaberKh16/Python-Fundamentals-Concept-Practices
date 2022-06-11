'''
    Non-Keyword Arguments Concept
    =============================
    #   Infinite Arguments or Non Keyword(*args) can use multiple number 
        of arguments just using the single argument specification which 
        is basically the array of arguments.
        
    #   Non Keyword Arguments can send as many numbers of data/values  
        you wanted for the function and can set as a single parameter. 
        
    #   By convention Non-keyword Argument use --> *args to specify 
        the argument, but any name can be set as the Non-Keyword Argument.
'''

# defining the function
def person_info(*persons):
    # need to loop to iterate throgh the *person args
    for person in persons:
        print(f"Person name is:{person}")
        
# passing multiple value to the single parameter '*person' 
persons = person_info("JK", "RK", "HK", "GK", "CK") 


