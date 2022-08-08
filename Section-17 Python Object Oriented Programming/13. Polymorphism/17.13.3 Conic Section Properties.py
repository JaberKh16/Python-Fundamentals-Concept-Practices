
class Parabola:
    name = 'Parabola'
    def __init__(self, x, y) -> None:
        self._vertex = (self.x, self.y)
        self._focus  = (self.x, self.y)
        self._directrix = (self.x, self.y)
    
    def calculate_properties(self):
        directrix_to_vertex = self.distance_from_directrix_to_vertex()
        vertex_to_focus = self.distance_from_vertex_to_directrix()
        if directrix_to_vertex == vertex_to_focus:
            print()
    
    def distance_from_directrix_to_vertex():
        pass
        
    
    def distance_from_vertex_to_directrix():
        pass
            

class Ellipse:
    name = 'Ellipse'
    def __init__(self, x, y, a, b) -> None:
        self._center = (self.x, self.y)
        self._major_axis = self.a if self.a > self.b else self.b 
        self.minor_axis = self.b if self.b > self.a else self.a
    
    def calculate_properties(self):
        pass

class Hyperbola:
    name = 'Hyperbola'
    def __init__(self, x, y, a, b) -> None:
        self._center = (self.x, self.y)
        self._focal_axis = self.a if self.a > self.b else self.b
        self._conjugate_axis = self.b if self.b > self.a else self.a
    
    def calculate_properties(self):
        pass