"""
 Class Method:
  
   a) class method can denoted by @classemethod decorator.
   b) class method has one initial parameter like the instance method parameter 'self' 
      by convention Python use 'cls' as a parameter, but can use any name.
      e.g -->   @classmethod
                def method(cls):
                    pass
   c) class method receives the class itself, implicitly though 'cls' parameter , just like
      an instance method receive the instance of class through 'self' parameter.                
   d) class method can be invoke using the class name or an instance of the class,
      but good practice to call via class name.
   e) class method can work only with the class variables/attributes and it can't
      access instance variables/attributes though it doesn't have 'self' parameter
      with it.Means class method is bound to class only , not the object of the class.
      
   f) Common use of class method is to define factory methods, as we know we can't
      overload function in Python, that means we can't have more __init__() initializer
      method in single class, but we can define another initializer method which
      is called the alternative initializer method using class method, typically this
      is the factory method. 
   g) Factory method is used to create instance object in different ways.
    
   
 
"""
class Person:
    # class attributes
    species = 'Homo Sapiens'
    count = 0
    
    # instance method 
    def __init__(self, name , age) -> None:
        self._name = name
        self._age = age
        self._email = '{}@gmail.com'.format(self._name)
        Person.count +=1
        
    # instance overloading method
    def __str__(self):
        return f'Name is :{self._name} ,Age is : {self._age} and Email : {self._email}'
    
    #class method are defined here
    @classmethod
    def show_count(cls):
        print(f'there are {cls.count} {cls.species}')

# calling the class attributes/methods
Person.show_count()

# creating instance of class
person_1 = Person('HK', 23)
Person.show_count()
print(person_1)
person_2 = Person('RK', 27)
Person.show_count()
print(person_2)

# calling via instance of class
person_1.show_count()
