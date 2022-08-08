"""
    Issues With Class When 'self' Not Specified
"""

# defining the class
class Employee:
    
    try:
        name = 'Jagri'
        age  = 29
        salary = 20000
    
        def get_salary():
            return salary
    
    except Exception as e:
        print(e)

# creating an object or instance for the specified class
emp_1 = Employee()

# now we will encounter a error why so,, because whenever a object is 
# getting created Python automatically instantiated an 'self' associated 
# with that object to define that this is that specific class object
print(emp_1.get_salary()) 