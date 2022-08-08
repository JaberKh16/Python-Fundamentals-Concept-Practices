'''
  Subclassing (Calling constructor of parent class)
   A child class needs to identify which class is it's parent class. This can be
   done by mentioning the parent class name in the definition of the child class.

   e.g   class sub_class_name(superclass_name)

   Note: If you forgot to invoke the __init__() of the parent class then it's instance
         variables/attributes would not be available to the child class.

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
        # invoking parent class __init__() initializer method to the child class
        Person.__init__(self, name, idnumber)
        # accessing parent class instance method display()
        print(self.display())
    def _employee_info(self):
        print('Salary is: %d and Post is: %s' %(self._salary, self._post))



b = Employee("Rahul", 368616, 15000, "assistant manager")
b.display()
b._employee_info()



