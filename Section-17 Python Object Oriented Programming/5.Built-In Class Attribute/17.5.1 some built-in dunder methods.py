'''
  # Python has some built-in class attributes
  # they can access by dot(.) like any other attributes
  # some built-in class attributes are--

        1. __dict__    --> containing the class namespaces
        2. __doc__     --> class documentation string or name is defined
        3. __name__    --> class name
        4. __class__ is a reference to the type of the current instance
        5. __module__  --> module name in which the class is defined
                           this attribute is "__main__" in interactive mode
        6. __bases__   --> A possibly empty tuple containing the base classes,
                           in the order of their occurrence in the base class
                           list
'''

class Employee:
    "Common base class for all employees"

    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount+=1

    def displayCount(self):
        print ("Total Employee %d" , "" %Employee.empcount)

    def displayEmployee(self):
        print("Name : ", self.name, "Salary :", self.salary)

# __doc__ will returns the docstring anything written inside the program,
# Employee.__doc__ means inside the class docstring 
print("Employee.__doc__ : ",Employee.__doc__ )
# Employee.__name__ will returns the class name
print("Employee.__name_ :",Employee.__name__)
# __class__ is a reference to the type of the current instance
print("Employee.__class__ :",Employee.__class__)
# __module__ will returns the module name in which the class is defined
print("Employee.__module__ :",Employee.__module__)
# __bases__ will returns the base of the class which is basically the object of the class
print("Employee.__bases__ :",Employee.__bases__)
# __dict__ will return all information in dict formatted for the class 
print("Employee.__dict__ :",Employee.__dict__)
