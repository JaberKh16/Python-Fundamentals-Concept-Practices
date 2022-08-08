"""
      Instance Attributes And Local Attributes Concept
      ================================================
      Instance Attributes are those which generally are being defined 
      inside a class methods and having the keyword 'self' thus its 
      has its scope throughout the class.

      Local Attributes are those attributes which is defined only inside 
      the class methods and has no 'self' keyword with them while defining.
      These are the temporary variables for the class methods and has its 
      scope only inside the methods where its being defined, thus can't be 
      accessible outside that class method. Local Attributes can't be accessed
      through class instance or class name.
      
"""

# defining the class
class Test:
      def method1(self):
            x = 12 # local attributes or variable
            print(x)

      def method2(self):
            self.y = 10 # instance attributes or class variable
            print(self.y)

# creaing the class instance
t1 = Test()
# calling the instance methods
t1.method1()

# assigning new value to instance attribute y
t1.y = 20

# see y value doesn't get change, why because there is no parameter been
# passed for the instance attribute 'y' to catch its values thus no 
# changes made for y
t1.method2() 