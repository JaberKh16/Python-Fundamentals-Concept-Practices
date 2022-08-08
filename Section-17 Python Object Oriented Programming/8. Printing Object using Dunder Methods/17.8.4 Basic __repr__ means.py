
class Test:
    def __init__(self,x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(self.__module__, 
                                                type(self).__name__, 
                                                hex(id(self))
                                                )

t1 = Test(14, 12)
print(t1)
print(t1.__repr__)