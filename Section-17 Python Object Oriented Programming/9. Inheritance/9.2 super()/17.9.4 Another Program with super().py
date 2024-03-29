"""
 Note : Using the base class names can cause real bugs in multiple inheritance. 
        If we use super(), the problem will not occur, super() used MRO.


"""

class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        self.id += 'T'
    
class Student(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        self.id += 'S'
   
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        Student.__init__(self,id)
        Teacher.__init__(self,id)
       
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)
