'''
  # In Python, from printing object if no __repr__ is defined then default
    is being used, which is basically the repr(obj) returns format, 
    means the object along with its location formatted as --
              <__main__.Test object at hex_location>
              

'''

class Test :

    def __init__(self, a, b):
        self.a = a
        self.b = b


t = Test(1234, 5678)
print(t)
