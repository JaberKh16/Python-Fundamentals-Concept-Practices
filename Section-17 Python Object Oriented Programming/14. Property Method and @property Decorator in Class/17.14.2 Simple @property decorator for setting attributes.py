
class Product:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
    
    def display_product(self):
        print(f'X is :{self._x} and Y is :{self._y}')
        
    @property
    def value(self):
        return self._x
    
    @value.setter
    def value(self, value):
        self._x = value
    

p = Product(12, 14)
p.display_product()

# setting a new value for X only
p.value = 10
print(f'Updated value for X is : {p.value}')