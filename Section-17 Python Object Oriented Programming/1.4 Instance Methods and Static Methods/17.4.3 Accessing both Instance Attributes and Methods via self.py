"""
  Accessing Instance Attributes and Instance Methods
  ===================================================
  # Inside a class all instance attributes and methods are only accessible 
    via class instance object which is 'self' basically.
    
    Means, whatever instance attributes or instance methods needed to be 
    initialized or called must be done like the following way-  
          
          1.  self.instance_attributes # accessing instance attribute with 'self'
          2.  self.instance_methods # accessing instance methods with 'self'

"""

# defining the class
class Test:
      def method1(self):
          print('Inside method1')
      
      def method2(self):
          print('Inside method2')
          # need to be initialize with self.method1,
          # otherwise will get an NameError: Not Defined
          # e.g - method1() this will give an error
          self.method1() # accessing another class instance method

# creating class instance
t = Test()

# accessing class instance method
t.method2()