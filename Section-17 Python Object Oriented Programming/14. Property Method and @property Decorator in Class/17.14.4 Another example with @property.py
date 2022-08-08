class Employee:
    def __init__(self, name, password, salary) -> None:
        self.name = name
        self._password = password
        self._salary = salary
    
    # getter or readonly method though setter method isn't defined
    @property
    def name(self):
        return self.name
    
    # read and writable method for attribute '_password'
    # getter or readonly method
    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    # setter or writeonly 
    @password.setter
    def password(self, new_password):
        self._password = new_password
    
    # setter or writeonly method for attribute '_salary'
    @property
    def salary(self,new_salary):
        self._salary = new_salary
        


try:
    # creating class instance
    emp = Employee('JK', 'jkr@@123', 55000)

    # accessing instance attributes
    emp.name

except Exception as e:
    print(e)


