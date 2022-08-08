
class Person:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age  = age
        self._email = email
    
    def info(self):
        print(f'Name is : {self.name}')
        print(f'Name is : {self.age}')
        print(f'Personal Email is : {self._email}')
        

class Teacher(Person):
    
    # though this class has no initializer __init__() method , so it used the
    # parent class __init__() method.
    
    # Now, info(self) its overriding method , though this class has the 
    # info() method so it will call its info() method, 
    # otherwise if this doesn't have the info() method , then it will call its 
    # inherited info() method from its parent class
    def info(self):
        print(f'Name is : {self.name}')
        print(f'Name is : {self.age}')
        print(f'Personal Email is : {self._email}')
     
       
t = Teacher('Ashik Ashkari', 34, 'ashik_faculty@.bscse.uiu.ac.bd')
t.info()
