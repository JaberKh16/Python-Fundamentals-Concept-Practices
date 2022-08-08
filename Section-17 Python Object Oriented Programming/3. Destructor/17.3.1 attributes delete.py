'''
   # Python has destructor also
   # We can delete attributes and objects itself via destruction
   # del operator is used for deletion or destruction
   # In destruction the object is however continues to memory until we
     specify new name to the object

     If no name is specified later for the object then later it get's
     destroyed, here new topic comes garbage collection----
   # What is Garbage Collection?

     The automatic destruction of unreferenced object in python is called
     garbage collection

   # What the use of this term garbage collection??

    By this process of destruction python reclaims blocks of memory that are
    no longer in used

    this garbage collector runs during programme execution and it is
    triggered when object's reference counts to zero(0).

    An object's reference count to changes as the number of aliases that
    points to it changes.

  # When does an object reference count start or increase else decrease??

    An object's reference count increases when it is assigned a new name or
    placed in a container(list, tuple, dict).

    The objects reference count decreases when it's deleted with del
    what happens then ??, it reference is reassigned or it's reference goes
    out of scope

    When a object's reference count to zero(0) , python collects it
    automatically.



'''

class Calculator :
    name = "Calcu"
    model = "FX 990T"
    battery =  5

    def calculation(self):
      print("I can do calculation")

c1 = Calculator()
try :
    # deleting the instance attributes of the class
    del c1.name
    del c1.battery


except:
    print("Specified attribute gets deleted")
    print(hasattr("Calculator", "name"))
    print(hasattr("Calculator", "battery"))



