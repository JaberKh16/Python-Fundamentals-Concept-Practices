class Person:
    def greet(self):
        print('I am a Person')
 
class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')
 
class Student(Person):
    def greet(self):
        # this classname.great() will call the 'Person' class great() method
        Person.greet(self)    
        print('I am a Student')
 
class TeachingAssistant(Student, Teacher):
     def greet(self):
         # this super() will call its parent method great()
         # here , though having 2 classes as parent class , ordering will be
         # followed is left to right , means 'Student' class will be followed.
         super().greet()
         print('I am a Teaching Assistant')

# creating instance of class       
x = TeachingAssistant()
x.greet()

print('============================================================')
# check the mro for prove
help(TeachingAssistant)