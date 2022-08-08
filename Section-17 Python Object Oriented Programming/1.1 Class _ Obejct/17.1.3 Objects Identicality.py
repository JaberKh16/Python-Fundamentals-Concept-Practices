"""
  Object Identity Concept
  ========================
  # A class can have many objects, typically N no. of objects.
  # Each objects for a particular class is identical means each 
    objects are unique in nature thus having unique identity means
    having a different memory location inside the RAM.
  

"""


# defining the class
class Test:
    pass

# creating two instance of the class
t1 = Test() # first instance of the class
t2 = Test() # second instance of the class

# t1 , t2 both are class objects but as they are identical objects
# both objects having different memory location, so they are 
# not having same identity(id)
print(t1 == t2, end=' ') 

# t1, t2 both are object type
print(type(t1) == type(t2), end=' ')