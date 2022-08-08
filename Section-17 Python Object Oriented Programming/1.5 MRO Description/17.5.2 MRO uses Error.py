"""
    MRO Explains Chaining Of Methods Concept
    ========================================
    # Chaining Of Classes can be happend the following-

        class Object:
            pass
        class class_name1:
            pass
        class class_name2(class_name1):
            pass
    
"""

class Person:
    def intro(self):
        """
            If this method gets deleted then will ask for its Base Class 
            method where the base class is class 'Object' and this 
            class 'Object' has no method named- intro(self), so will through an AttributeError. 
        """
        print('I am Person')

class Teacher(Person):
    def intro(self):
        """
            If this method gets deleted then will ask for its Base Class 
            which is class 'Person' here, because inheriting the 'Person'
            class and ask for the intro() method in Person class.
        """
        print('I am a Teacher')

class Student(Person):
    def intro(self):
        """
            If this method gets deleted then will ask for its Base Class 
            which is class 'Person' here, because inherting the 'Person'
            class and ask for the intro() method in Person class.
        """
        print('I am a Student')

class Teaching_Assistant(Student, Teacher):
    pass

# creating class instance
TA = Teaching_Assistant()
TA.intro()