'''
  Class Constructor __init__() Concept
  ====================================
  # class function that begins with a double underscore(__) actually called
    a special function in Python.
  # One of them are ,  __init__() function which is the class constructor.
  # Basically it's constructor in Python OOP.
  # Whenever a new object of class is instantiated constructor get's called
    automatically.
  # Constructor can be used to initialize values for instance attributes.

'''

# defining the class
class ComplexNumber :
    # __init__() with default value arguments
    def __init__(self, r =0 , i =0):
        self.real = r # real numbers
        self.imag = i # imaginary numbers
        # note: 1. self.real and self.imag are the origianl class attributes
        #       2. r , i is the dummy arguments 

    # making the setters or can say the mutators
    def set_Real_Data(self, value):
        self.real = value
    def set_Imag_Data(self, value):
        self.imag = value

    # making getters or can say inspectors
    def getData(self):
        # index value {0} = self.real
        # index value {1} = sign
        # index value {2} = self.imag
        if self.real and self.imag > 0:
          sign = '+'
          print("{0}i {1} {2}j".format(self.real, sign, self.imag))
        else:
          sign = '-'
          print("{0}i {1} {2}j".format(self.real, sign, -self.imag))
        
        return  (self.real, sign, self.imag)
      
      
      
# creating ComplexNumber object
# for positive numbers
c1 = ComplexNumber(2, 3)
# getting the data using getData()
c1.getData()
# for negative numbers
c2 = ComplexNumber(8, -5)
# getting the data using getData()
c2.getData()


# c3 = ComplexNumber()
# c3.attr = 10 # setting the instance attributes using object.attr = value
# print((c2.real, c2.imag, c2.attr))

c4 = ComplexNumber()
c4.set_Imag_Data(3) # setting imaginary data to 3 for object c3
c4.set_Real_Data(4) # setting real data to 4 for object c3
print("Real & Imaginary Value is :" ,c4.getData())