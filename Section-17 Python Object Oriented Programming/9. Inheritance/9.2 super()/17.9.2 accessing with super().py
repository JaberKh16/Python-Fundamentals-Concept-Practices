
"""
  Note: super() followes MRO technique to ordering the class attributes.

"""

class Mother:
    def cook(self):
        print('Can cook pasta')
 
class Father:
    def cook(self):
        print('Can cook noodles')
 
class Daughter(Father, Mother):
    pass
 
class Son(Mother, Father):
    def cook(self):
        # with super() doesn't need to invoke 'self' with instance or class methods
        super().cook()
        print('Can cook butter chicken') 

# creating instance of class 
daughter = Daughter()  
son = Son()
 
daughter.cook()
print() # this will print a new line
son.cook()