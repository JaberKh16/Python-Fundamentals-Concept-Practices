'''
    Non-Keyword Argument Type
    =========================
    # Basically, Non Keyword Argument generates a 'tuple' data type.
'''

# defining the function
def person_info(*persons):
    return persons    
        
# passing multiple value to the single parameter '*person' 
persons = person_info("JK", "RK", "HK", "GK", "CK") 
print(f"Non Keyword Argument Data Type: {type(persons)}")
print(f"Person name is:{persons}")
