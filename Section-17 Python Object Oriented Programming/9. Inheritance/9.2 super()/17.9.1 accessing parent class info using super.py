'''
 # Super function is a built-in function .
 # it is used to return a proxy object that delegates method calls to a parent
   or sibling class of type
   this is useful for accessing inherited methods that have been overridden in
   a class

 # Syntax - super().methodName(arg1, arg2, ...)      --->  in Python 3
          - super(subclass, instance).method(args)    ---> in Python 2

 # In Python, super() built_in has two major use case -

     1. Allow us to avoid using base class explicitly.
     2. Working with Multiple Inheritance
 # To work with the super() we need to first define the class attributes from
   base class into the child class and then initialize it with super() function

'''

# super() with single inheritance

class Person :
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person) :
    def __int__(self, first_name, last_name, email):
        #super().__init__()
        self.email = email
    def get_employee_info(self):
        super().Name()
        self.email = '{}@gmail.com'.format(self.firstname)
        return self.Name() + "\n" + self.email


employee = Employee('Jacob','Rachen')
print(employee.Name())
print(employee.get_employee_info())


