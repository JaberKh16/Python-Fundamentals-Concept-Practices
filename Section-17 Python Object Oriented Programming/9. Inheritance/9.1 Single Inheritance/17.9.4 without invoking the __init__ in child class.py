class A :
    def __int__(self, name= "Rahul"):
        self.name = name

class B (A) :
    def __int__(self, roll):
        self.roll = roll
        print(self.roll)
 
try:
    b = B()
    # can't access the parent class instance attribute 
    # though we didn't invoke __init__() of parent class to child class
    print(b.name)
except Exception as e:
    print(e)
    

