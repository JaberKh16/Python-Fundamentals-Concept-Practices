"""
 Property:
  
  -->Properties can be considered the "Pythonic" way of working with attributes.
    
   1. @property is a built-in decorator for the property() function in Python. 
   2. denoted by @property keyword.
   3. It is used to give "special" functionality to certain methods to make them act as 
      getters, setters, or deleters when we define properties in a class.
   4. It's used to define properties in the Python class, and it encapsulates
      instance attributes and provides a property.
   5. @property makes a instance method, instance variable , means the
      class instance methods can be accessed as like instance variable access.
   6. with @property , accessing instance attributes exactly as if they were public attributes
      while using the "magic" of intermediaries (getters and setters) to validate new values 
      and to avoid accessing or modifying the data directly. 


"""

class House:
    def __init__(self, name, price) -> None:
        self.name = name
        # protected attributes
        self._price = price
    
    # if you want to add setters and getters that each line of code that
    # accesses or modifies the value of the attributes that also needs 
    # to be modified to access the setters or getters otherwise the code will break. 
    def get_price(self):
       print(f'Price is : {self._price}')
    
    def set_price(self, new_price):
       """
       set the price
       """
       self._price = self.new_price 
       


# creating class instance
house = House('Georgia', 45000)

# accessing class instance attributes
print(f'Price of the house is :{house._price}')

# modifying the attributes value, while its shouldn't be permissible 
# because the attribute is protected.
house._price = 50000  
print(f'Price of the house is :{house._price}')

# getting the price 
house.get_price()

# setting the price again
try :
   house.set_price(60000)
   house.get_price()
except  Exception as e:
   print(e)