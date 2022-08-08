'''
  # Inheritance is the capability of one class to derived or inherit the properties
    from some other class(e.g parent class)

  # this gives the ability to child class to inherits all the attributes of it's
    parent class, can use those attributes as if they were defined in child class

  # A child class can also override data members and methods from the parent class

  # Syntax : sub_class_name (Parent_class_name1, Parent_class_name2, ...)

  # Some benefit from the inheritance --

     1. it represents the real world relationship as well
     2. it provides reusability  of a code .We don't have to write same code
        again and again. Also, it allows us to add more features to class
        without modifying it

     3. it is transitive in nature , which means if class B inherits from another
        class A , then all the subclasses of B would automatically inherit
        from A


'''

class Person :

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person) :
    # though we dont have any __init__ method here, but this class inheritted
    # all attributes and methods from the Person class, so this class gets
    # the __init__() too from the Person class. 
    def isEmployee(self):
        return True

# making object of parent class
jhon = Person("Jhon")
print(jhon.getName(), jhon.isEmployee())


# making object of child class
jacob = Employee("Jacob")
print(jacob.name)
print(jacob.getName(), jacob.isEmployee())

