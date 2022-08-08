
class Rectangle:
    # instance method
    def __init__(self, width, height) -> None:
        # protected attributes
        self._width = width
        self._height = height
    # instance method
    def calculated_area(self):
        return self._width * self._height
    
    # class method
    @classmethod
    def new_square(cls, side_length):
        # local variable
        _side_length = side_length
        return cls(_side_length, _side_length)
    

# calling class method via class name
square = Rectangle.new_square(5) 
print(square.calculated_area())