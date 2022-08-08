'''
 Convention about Protected Attributes and Methods in Python --- 
   # accessing protected instance attributes outside the class
   # thought python gives the access to the protected attributes for debugging purpose,
   # but its not good convention to access the protected attributes and method outside the class

'''


class Person :

    def __init__(self, name , idnumber):
        # protected instance attributes
        self._name = name
        self._idnumber = idnumber

    def display(self):
        return 'Name is: %s and Id is: %d' %(self._name, self._idnumber)
        


class Employee(Person) :

    def __init__(self, name, idnumber, salary , post):
        # protected instance attributes
        self._salary = salary
        self._post = post
        # accessing parent class __init__() initializer method
        Person.__init__(self, name, idnumber)
        # accessing parent class instance method display()
        print(self.display())
    def _employee_info(self):
        print('Salary is: %d and Post is: %s' %(self._salary, self._post))



a = Employee('Jaber', 161188)
# accessing protected instance attributes
a._name
a._idnumber
print('=========================================================')


b = Employee("Rahul", 368616, 15000, "assistant manager")
b.display()
# accessing protected instance method
b._employee_info()



