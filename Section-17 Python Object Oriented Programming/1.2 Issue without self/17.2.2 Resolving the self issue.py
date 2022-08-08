"""
    Resolving The 'self' Issue
    ==========================
    #   Class methods have only one specific difference from an 
        ordinary functions and that is why they must have an 
        extra parameter, which refers to the object itself.
    
    # For Example : 
        when called a method like -
            object.function_name(num1, num2)
            this(object) is automatically converted by Python into
                class_object(object, num1, num2)
            means the object is automatically passed as a paramter to the
            class and save into the 'self' which called the instance object
            that invokes the method.   
"""

# defining the class
class Employee:
    name = 'Jagnri'
    age = 29
    salary = 20000
    
    def get_salary(self):
        return self.salary
    
    def get_the_full_info(self):
        print(f'Name is :{self.name} , Age is :{self.age} and the Salary is:{self.salary}')
    
# creating the class instance
emp_1 = Employee()
print(emp_1.get_salary())   
print(emp_1.get_the_full_info()) 