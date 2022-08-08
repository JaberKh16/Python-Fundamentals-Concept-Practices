
"""
 Factory Methods:
   
   a)Common use of class method is to define factory methods, as we know we can't
      overload function in Python, that means we can't have more __init__() initializer
      method in single class, but we can define another initializer method which
      is called the alternative initializer method using class method, typically this
      is the factory method. 
   b) Factory method is used to create instance object in different ways.

"""
class Person:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
    
    def __str__(self) -> str:
        return 'Name is : {0} and Age is : {1}'.format(self._name, self._age)
    
    # class method as initializer(factory) method for string datatype
    @classmethod
    def from_string(cls, s):
        _name, _age = s.split(',')
        return cls(_name, int(_age))
    
    # class method as initializer(factory) method for dictionary datatype 
    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])
    

# creating instance of class
person_1 = Person('JK', 25)
print(person_1)
person_2 = Person('RK', 34) 
print(person_2)

# creating string datatype
s = 'FK, 45'
person_3 = Person.from_string(s)
print(person_3)

# creating dictionary datatype
d = {'name':'BK', 'age':28}
person_4 = Person.from_dict(d)
print(person_4)