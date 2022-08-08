"""
    Python Class MRO 
    ================
    a) Why Need MRO:

        #   When multiple or multilevel, hierarchal inheritance are available 
            in same class, that time the structure become more complex, and 
            searching for attributes in Base class doesn't remain 
            straightforward.

        #   So to resolve any sort of conflict while searching for attributes 
            in Base classes, Python uses the order in which Python searches 
            for attributes in Base classes, which is basically called the 
            Method Resolution Order(MRO).
    
    b) Uses of  MRO :

        #   Order in which Python searches for attributes in base classes.
        #   It gives a linearized path for an inheritance structure.
        #   So, Python computes an MRO, for every class in the hierarchy 
            and the MRO is computed using the 'C3 Linearization Algorithm' 
            which is much complex structure.
            
            But roughly it works like 'Depth First Search' in left to right 
            manner and searches for each classes only once.
        
    c) To see MRO of a class:
        
            # classname.__mro__ ---> tuple format
            # classname.mro()   ---> list format
            # help(classname)   ---> Help Format
            # instance.__class__.__mro__

"""

# defining classes
class Person:
    pass

class Teacher(Person):
    pass

class Student(Person):
    pass

class Teaching_Assistant(Student, Teacher):
    pass


while True:
    TA = Teaching_Assistant()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        # return as Help Formatted
        print(f"MRO for 'TA' instance in Help Format :{help(Teaching_Assistant)}")
    elif choice == 2:
        # return as Tuple Formatted
        print(f"MRO for 'TA' instance in Tuple Format:{Teaching_Assistant.__mro__}")
    elif choice == 3:
        # return as List Formatted
        print(f"MRO for 'TA' instance in List Format :{Teaching_Assistant.mro()}")
    elif choice == 4:
        # return as Tuple Formatted
        print(f"MRO for 'TA' instance in :{TA.__class__.__mro__}")
    elif choice == 0:
        print('Exiting the Program...........')
        exit()