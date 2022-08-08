# implementing own property class
class My_Property:
    def __init__(self, func) -> None:
        self._func = func
    
    # here, basically,  inst = instance
    def __get__(self, inst, owner=None):
        return self._func(inst)
    
# creating another class 
class Location:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    # @property defined which is our defined property
    @My_Property
    def location(self):
        return [self.x, self.y]
    
    
    def move_left(self):
        self.x -= 1
        
    def move_right(self):
        self.x += 1 
    
    def move_up(self):
        self.y -= 1
        
    def move_down(self):
        self.y += 1
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(x={self.x}, y={self.y})'
    

# creating class instance
loc = Location()
print(f'Location is : {loc}')
# accessing instance methods
loc.move_left()
print(loc.location)
print(f'New Location is : {loc}')

loc.move_down()
print(loc.location)
print(f'New Location is : {loc}')

