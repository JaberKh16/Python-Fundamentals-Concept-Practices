"""
    Python Class Attributes and Methods Inclusion
    ===============================================
    Python Classes provides the facilties to include class 
    attributes outside the class. Doesn't support class 
    methods inclusion outside the classes and hits an 
    exception called- AttributeError.
    
"""

# defining the class
class Person :
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        print("Name : ", self.name, "\n" "ID :", self.idnumber)
    def isEmployee(self):
        return False

m = Person("Jaber", 161188)
print(f'Employee or not : {m.isEmployee()}')

print("\n")

# adding new attributes to the class
m.known_language = "Python"
print(m.known_language)

# adding new method to the class

'''

m.workframe()
print(m.workframe("Basics Knowledge"))

# well it's give an error called- AttributeError: class has no attribute 'workframe()'
# Python doesn't supports methods inclusion from outside the class.

'''
