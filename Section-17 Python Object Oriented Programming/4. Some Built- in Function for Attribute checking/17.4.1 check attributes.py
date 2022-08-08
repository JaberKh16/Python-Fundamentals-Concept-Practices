'''
  # Python class object has some built-in function
  # it is used to check for the attributes and work on attributes
  # Some built-in functions are --

          1. hasattr (obj, attribute_name)
           --> check if an attribute is exist in object class
          2. getattr (obj, attribute_name [, default])
           --> to access the attribute of object class
               which returns the specified attribute value
          3. setattr (obj, attribute_name , value)
           --> to set a new attribute in object class with initializing,
               if one exist then with the same then new specified value
               gets initialized
          4. delattr (obj, attribute_name)
           --> to delete an attribute from the object class


'''

class Bank :
    name = "SouthEast Bank"
    branch = "Banani"
    Ip_address = "173.103.65.63"

    def full_time_Employee(self):
        print("full time")

    def half_time_Employee(self):
        print("half time")

person = Bank()
#check via class name
print(hasattr(Bank, "name"))
#check via newly created object 
print(hasattr(person, "name"))

print(getattr(person, "branch"))
print(getattr(Bank, "branch"))

# with non existing attribute
# setting new instance attribute 'work' with a value
setattr(person, "work", "financial bank")
print(hasattr(person, "work"))
print(getattr(person, "work"))

# with existing attribute
# setting the previous instance attribute 'Ip_address' to new value
setattr(person, "Ip_address", "131.234.31.13")
print(hasattr(person, "Ip_address"))
print(getattr(person, "Ip_address"))

# delete an existing attribute
setattr(person, "income", 1500000)
print(getattr(person, "income"))
print(hasattr(person, "income"))
print(delattr(person, "income"))
print(hasattr(person, "income"))








