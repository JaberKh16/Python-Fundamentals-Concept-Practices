
class Test:
    # class attributes
    x = 7
    def __init__(self, x1, x2) -> None:
        self.x1 = x1
        self.x2 = x2
    
    
    def get_value(self):
        return f'X1 is : {self.x1} and X2 is : {self.x2}' 
    
    # class method with 'self' as parameter
    @classmethod
    def get_value(self):
        print(self.x)

test_1 = Test.get_value()
test_1

test_2 = Test(5, 10)
# see the result , why same ? because here @classmethod also use 'self' as parameter
# which will call the class itself via self, thought we have a class attribute x
test_2.get_value()