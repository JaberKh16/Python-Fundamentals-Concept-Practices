''''
    # In Python , from printing object if we didn't use __str__ then
      print(t) will use __repr__

'''

class Test :

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a : %s, b : %s" %(self.a, self.b)

t = Test(1234, 5678)
print(t)
