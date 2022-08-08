class Location:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    @property
    def location(self):
        return [self.x, self.y]
    
    @location.setter
    def location(self, new_location):
        self.x , self.y = new_location
    
    @location.deleter
    def location(self):
        self.x = self.y = 0
        
    def move_left(self):
        self.x -= 1
        
    def move_right(self):
        self.x += 1 
    
    def move_up(self):
        self.y -= 1
        
    def move_down(self):
        self.y += 1
    
    def __repr__(self) -> str:
        # type(self) is the class which is <class '__main__>
        # type(self.__name__) is the current class object name which is <class '__main__.object'>
        return f'{type(self).__name__}(x={self.x}, y={self.y})'
    

# creating class instance
loc = Location()
print(f'Location is : {loc}')

# setting a new location
loc.location = [1000, 300]
print(f'Updated Location is: {loc}')

# deleting the location
try :
    # deleting the location
    del loc.location
    print(f'After deletion location is: {loc}')
except Exception as e:
    print(e)

finally:
    # creating another location
    loc.location = [500, 100]
    print(f'Created Location is: {loc}')