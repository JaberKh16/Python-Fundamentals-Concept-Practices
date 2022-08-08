
class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    # here, __add__ (self, other)
    # first, 'self' is the first object class and 
    # second, 'other' is the second object class    
    def __add__(self, other):
        return (self.num1 + other.num1 , self.num2 + other.num2)
    
    def __sub__(self, other):
        return (self.num1 - other.num1, self.num2 - other.num2)
    
    def __mul__(self, other):
        return (self.num1 * other.num1, self.num2 * other.num2)
    

try:
    obj_1 = Calculator(3, 4)
    obj_2 = Calculator(4, 2)
    add = obj_1 + obj_2
    sub = obj_1 - obj_2
    mul = obj_1 * obj_2
    print(f'Summation is: {add}')
    print(f'Subtraction is: {sub}')
    print(f'Multiplication is: {mul}')

    
except Exception as e:
    print(e)


