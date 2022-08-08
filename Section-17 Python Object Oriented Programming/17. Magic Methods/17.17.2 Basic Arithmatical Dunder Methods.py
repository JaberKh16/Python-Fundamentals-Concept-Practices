"""
 Static Method:
 
   # Static method are created using @staticmethod decorator.
   # The @staticmethod is a built-in decorator in Python which defines a static method.
   # Static method is the helper or utility method, that contains some logic related 
     to class.
   # Static method doesn't need to access class variables nor instance variables.
   # Static method is just like a regular function , but it belongs to the class
     namespace.

"""

class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        
        if self.denominator < 0:  
            self.numerator *= -1
            self.denominator *= -1
        self._reduce()
 
    def show_result(self):
        print(f'Result is : {self.numerator}/{self.denominator}')
 
    def __mul__(self,other):
        # here, other is object of class, 
        # isinstance(object, classinfo) return True or False
        # object to be checked here its 'other'
        # classinfo = class, tuple, any datatypes
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction(self.numerator * other.numerator , self.denominator * other.denominator)
        f._reduce()
        return f
        
    def __add__(self,other):
        if isinstance(other,int):
            other = Fraction(other)
            
        # adding in fraction is like --> ( ( nr * dr ) + (nr * dr) ) /(dr * dr) 
        # adding is like 1/6 + (-1)/6 ---> ( (1 * 6) + (-1) * 6) ) / 6
        f = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        f._reduce()
        return f
    
    def __sub__(self,other):
        if isinstance(other,int):
            other = Fraction(other)
            
        # adding in fraction is like --> ( ( nr * dr ) + (nr * dr) ) /(dr * dr) 
        # adding is like 1/6 + (-1)/6 ---> ( (1 * 6) + (-1) * 6) ) / 6
        f = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        f._reduce()
        return f
 
    def _reduce(self):
        # calling static method hcf via class name
        h = Fraction.hcf(self.numerator, self.denominator)
        if h == 0:
            return
        # '//' means i want a integer value only
        self.numerator = self.numerator // h
        self.denominator = self.denominator // h
        
    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s = s - 1
        return s
 
       
f1 = Fraction(6,36)
f1.show_result()
f2 = Fraction(2,-12)
f2.show_result()
f3 = f1.__mul__(f2)
f3.show_result()
f3 = f1.__add__(f2)
f3.show_result()
f3 = f1.__add__(5) 
f3.show_result()
f3 = f1.__sub__(5) 
f3.show_result()
f3 = f1.__mul__(5) 
f3.show_result()
