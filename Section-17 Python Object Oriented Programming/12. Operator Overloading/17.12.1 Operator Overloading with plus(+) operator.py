"""
  '+' operator is basically the overlaoding operator (it works on different data types)

"""


class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        


try:
    obj_1 = Calculator(3, 4)
    obj_2 = Calculator(4, 2)
    obj_3 = obj_1 + obj_2  # adding to similar type object , here class objects
    print(obj_3) 
    
except Exception as e:
    print(e)


