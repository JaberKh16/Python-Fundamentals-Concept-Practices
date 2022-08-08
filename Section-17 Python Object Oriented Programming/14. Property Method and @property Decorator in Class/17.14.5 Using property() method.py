"""
 Property():
   
   In Python, property() is a built-in function that creates and returns a property object. 
   The syntax of this function is:

        property(fget=None, fset=None, fdel=None, doc=None)
        where,

            a) fget is function to get value of the attribute
            b) fset is function to set value of the attribute
            c) fdel is function to delete the attribute
            d) doc is a string (like a comment)
    
        these function arguments are optional. 
        So, a property object can simply be created as --> 
                       
                       p = property()
                       
   A property object has three methods, getter(), setter(), and deleter() to specify 
   fget, fset and fdel at a later point.. 
          


"""





# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature # this will called the temperature object

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter method
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter method
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    
    # creating a property object
    temperature = property(get_temperature, set_temperature)
    
    """ 
      
      Can also be Break down as like follows :
       
         # make empty property
         temperature = property()
         # assign fget
         temperature = temperature.getter(get_temperature)
         # assign fset
         temperature = temperature.setter(set_temperature)
    
    """
    
temp = Celsius(38)

# accessing the instance attribute
print(temp.temperature)
# accessing the instance method
print(temp.to_fahrenheit())

# setting instance attributes
temp.temperature = 45
print(temp.get_temperature())
print(temp.to_fahrenheit())
